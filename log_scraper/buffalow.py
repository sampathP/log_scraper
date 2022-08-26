#!/usr/bin/env python3
import time
from log_scraper import counters as c
from prometheus_client import write_to_textfile

# Define the dirctorys
logdir = '/var/syslog/hosts/buffalo.setup/'
text_exporter = '/var/lib/node_exporter/'


def tail_f(fname):
    f = open(logdir+fname, 'r')
    interval = 1.0
    while True:
        where = f.tell()
        line = f.readline()
        if not line:
            time.sleep(interval)
            f.seek(where)
        else:
            yield line


def daemon_log(fname):
    for line in tail_f(fname):
        e_items = line.split(' : ', maxsplit=1)
        if "message repeated" in e_items[0]:
            repeat = int(e_items[0].split()[6])
        else:
            repeat = 1
        event = e_items[1].split()
        e_name = event[0][:-1]
        e_type = event[1]
        if e_name in ['FIREWALL']:
            c.daemon_c_fw.inc(repeat)
            if e_type == 'TCP':
                c.daemon_c_fw_tcp.inc(repeat)
            elif e_type == 'UDP':
                c.daemon_c_fw_udp.inc(repeat)
            elif e_type == 'ICMP':
                c.daemon_c_fw_icmp.inc(repeat)
            else:
                pass
            msg = {}
            msg['type'] = e_name
            msg['event'] = e_type
            msg['source_ip'] = event[5].split(':')[0]
            msg['source_port'] = event[5].split(':')[1]
            msg['dest_ip'] = event[7].split(':')[0]
            msg['dest_port'] = event[7].split(':')[1]
            c.daemon_fw_info(msg)
        if e_type in ['DHCPREQUEST', 'DHCPACK', 'DHCPOFFER']:
            msg = {}
            msg['type'] = e_name
            msg['event'] = e_type
            msg['ip'] = event[3]
            msg['mac'] = event[5]
            c.daemon_c_dhcps.inc(repeat)
            if e_type == 'DHCPREQUEST':
                c.daemon_c_dhcps_req.inc(repeat)
            elif e_type == 'DHCPACK':
                c.daemon_c_dhcps_ack.inc(repeat)
            elif e_type == 'DHCPOFFER':
                c.daemon_c_dhcps_offer.inc(repeat)
            else:
                pass
            c.daemon_dhcp_info(msg)
        write_to_textfile(
            text_exporter + 'buffalo_daemon_log.prom', c.registry)
        write_to_textfile(
            text_exporter + 'buffalo_daemon_log_gauge.prom', c.g_reg)


def user_log(fname):
    for line in tail_f(fname):
        e_items = line.spli(' : ', maxsplit=1)
        # No repeat found so far in the log
        # However, leve it as fail-safe
        if "message repeated" in e_items[0]:
            repeat = int(e_items[0].split()[6])
        else:
            repeat = 1
        event = e_items[1].split()
        e_name = event[0][:-1]
        if e_name == 'AUTH':
            c.auth_user.inc(repeat)
            c.g_auth_user.set(repeat)
        elif e_name == 'SYSTEM':
            c.sys_user.inc(repeat)
            c.g_sys_user.set(repeat)
        else:
            c.unknwon_count.inc(repeat)
            c.g_unknwon_count.set(repeat)
        c.info_cron.info({'message': e_items[1]})
        write_to_textfile(text_exporter + 'buffalo_user_log.prom', c.registry)
        write_to_textfile(text_exporter + 'buffalo_daemon_log_gauge.prom',
                          c.g_reg)


def cron_log(fname):
    for line in tail_f(fname):
        e_items = line.spli(' : ', maxsplit=1)
        # No repeat found so far in the log
        # However, leve it as fail-safe
        if "message repeated" in e_items[0]:
            repeat = int(e_items[0].split()[6])
        else:
            repeat = 1
        event = e_items[1]
        c.count_cron.inc(repeat)
        c.g_count_cron.set(repeat)
        c.info_cron.info({'message': event})
        write_to_textfile(text_exporter + 'buffalo_cron_log.prom', c.registry)
        write_to_textfile(text_exporter + 'buffalo_daemon_log_gauge.prom',
                          c.g_reg)


def main():
    # Set the filename and open the file
    daemon_fname = 'daemon.log'
    cron_fname = 'cron.log'
    user_fname = 'user.log'
    daemon_log(daemon_fname)
    user_log(user_fname)
    cron_log(cron_fname)


if __name__ == "__main__":
    main()
