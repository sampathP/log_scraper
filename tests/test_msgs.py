#!/usr/bin/env python
# -*- coding: utf-8 -*-

DHCPS_DHCPREQUEST = ['Aug  5 04:13:06 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPREQUEST for 192.168.11.111 from d4:3b:04:7d:3e:e4 (k190801262a) via br0']
# Aug  5 03:59:50 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPREQUEST for 192.168.11.66 from 00:1c:fc:4f:82:06 via br0
# """

DHCPS_DHCPACK = """
Aug  5 03:59:50 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPACK on 192.168.11.66 to 00:1c:fc:4f:82:06 via br0
Aug  5 04:13:05 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPACK on 192.168.11.111 to d4:3b:04:7d:3e:e4 (k190801262a) via br0
Aug  5 04:13:07 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPACK on 192.168.11.111 to d4:3b:04:7d:3e:e4 (k190801262a) via br0
Aug  5 04:46:47 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPACK on 192.168.11.64 to 48:5f:99:ca:36:49 (BRW485F99CA3649) via br0
"""
DHCPS_INFO = """
Aug  5 03:59:51 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Information-request message from fe80::21c:fcff:fe4f:8206 port 546, transaction ID 0x92BE5700
Aug  5 04:13:07 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Information-request message from fe80::61a1:1149:281:b4c1 port 546, transaction ID 0x27370D00
"""
DHCPS_SEND_ADV = """
Aug  5 04:13:06 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Sending Advertise to fe80::61a1:1149:281:b4c1 port 546
"""
DHCPS_SEND_REP = """{Aug  5 04:13:08 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Sending Reply to fe80::61a1:1149:281:b4c1 port 546"""
DHCPS_DHCPDISCOVER = """Aug  4 11:35:54 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPDISCOVER from d4:84:57:90:22:2e (Toshiba_db_222E) via br0
Aug  4 12:36:29 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPDISCOVER from 70:26:05:76:bb:fe via br0"""

DHCPS_DHCPOFFER = """Aug  4 13:52:56 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPOFFER on 192.168.11.89 to d6:16:72:d6:e9:c2 via br0
Aug  4 15:17:40 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPOFFER on 192.168.11.76 to c0:06:c3:df:bc:d1 (C200_DFBCD1) via br0"""

DHCPS_SOL = """Aug  5 04:13:05 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Solicit message from fe80::61a1:1149:281:b4c1 port 546, transaction ID 0xD0FCE00
Aug  5 04:13:05 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Solicit message from fe80::61a1:1149:281:b4c1 port 546, transaction ID 0xD0FCE00"""

DHCPS_UNKOWN = """
Aug  5 04:13:06 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Unable to pick client address: no IPv6 pools on this shared network"""

DHCPS_ICMP_ECO = """
Aug  2 11:17:47 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: ICMP Echo reply while lease 192.168.11.124 valid.
Aug  4 15:17:39 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: ICMP Echo reply while lease 192.168.11.127 valid.
"""
DHCPS_ABAN_IP = """Aug  2 11:17:47 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Abandoning IP address 192.168.11.124: pinged before offer
Aug  4 15:17:39 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: Abandoning IP address 192.168.11.127: pinged before offer"""

DHCPS_DHCPINFORM = """Dec  7 20:39:12 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPINFORM from 192.168.11.75 via br0"""
DHCPS_DHCPRELEASE= """Jul  8 02:59:24 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPRELEASE of 192.168.11.71 from 64:4b:f0:2b:5a:b2 (SamMacBookPro28) via br0 (found)
Jul 14 02:07:16 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPRELEASE of 192.168.11.119 from 52:54:00:66:63:cf via br0 (not found)"""
DHCPS_DHCPNAK = """Dec 30 04:15:51 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: DHCPNAK on 192.168.11.70 to 24:2e:02:51:bb:e2 via br0"""
DHCPS_UID = """Feb 20 02:37:51 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPS: uid lease 192.168.11.106 for client c0:06:c3:df:bc:d1 is duplicate on 192.168.11.0/24"""

FW_TCP_DROP = """Aug  5 04:34:31 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : FIREWALL: TCP connection denied from 20.198.118.190:443 to 106.73.1.97:65045 (map0)
Aug  5 04:34:44 buffalo.setup  message repeated 7 times: [[50:C4:DD:C0:66:F8] AP50C4DDC066F8 : FIREWALL: TCP connection denied from 20.198.118.190:443 to 106.73.1.97:65045 (map0)]
Aug  4 15:17:03 buffalo.setup  message repeated 2 times: [[50:C4:DD:C0:66:F8] AP50C4DDC066F8 : FIREWALL: UDP connection denied from 54.255.64.101:3479 to 106.73.1.97:56849 (map0)]
"""
FW_UDP_DROP = """Aug  4 15:17:03 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : FIREWALL: UDP connection denied from 54.151.176.117:3478 to 106.73.1.97:56849 (map0)"""

FW_ICMP_DROP = """Jul 12 13:15:19 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : FIREWALL: ICMP connection denied from 150.91.169.84:n/a to 106.73.1.97:n/a (map0)
Jul 12 13:15:24 buffalo.setup  message repeated 5 times: [[50:C4:DD:C0:66:F8] AP50C4DDC066F8 : FIREWALL: ICMP connection denied from 150.91.169.84:n/a to 106.73.1.97:n/a (map0)]
"""
DHCPC_XMT = """Aug  3 17:49:28 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPC: XMT: Info-Request on eth1, interval 1060ms.
Aug  4 17:49:28 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPC: XMT: Info-Request on eth1, interval 1030ms."""

DHCPC_RCV = """Aug  3 17:49:29 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPC: RCV: Reply message on eth1 from fe80::21e:13ff:fec3:9c3.
Aug  4 17:49:29 buffalo.setup  [50:C4:DD:C0:66:F8] AP50C4DDC066F8 : DHCPC: RCV: Reply message on eth1 from fe80::21e:13ff:fec3:9c3.
"""
