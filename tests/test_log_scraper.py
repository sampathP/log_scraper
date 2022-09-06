#!/usr/bin/e`xnv python
# -*- coding: utf-8 -*-

"""Tests for `log_scraper` package."""
import unittest
import unittest.mock as mock
try:
    from log_scraper import buffalow
except RuntimeError as e:
    print(e)
from tests import test_msgs as tm


class testlog_scraper(unittest.TestCase):
    # @mock.patch('__builtin__.open')
    # def setUp(self, m_open):
    #     pass

    @mock.patch('log_scraper.buffalow.tail_f')
    def test_FW_message(self, m_tail_f):
        buffalow.daemon_log("/dum/dum")
        m_tail_f.assert_called_with("/dum/dum")

    @mock.patch('log_scraper.buffalow.c')
    @mock.patch('log_scraper.buffalow.tail_f')
    def test_dhcp_dhcprequest(self, m_tail_f, mc):
        m_tail_f.return_value = tm.DHCPS_DHCPREQUEST
        mock_w2t = mock.MagicMock()
        with mock.patch('log_scraper.buffalow.write_to_textfile', mock_w2t):
            buffalow.daemon_log("/dum/dum")
        mc.daemon_c_dhcps_req.inc.assert_called()
       
    # @mock.patch('log_scraper.__builtin__.open')
    # def test_tail_f(self, m_open):
    #     m_open.return_value('file_content')
    #     buffalow.tail_f(m_open("/a/b/file.log"))

    # def test_tail_f(self):
    #     dt = 'readline1\nreadline2\nreadline3\n'
    #     mock_io = mock.mock_open(read_data=dt)
    #     with mock.patch('log_scraper.buffalow.open', mock_io):
    #         log_scraper.buffalow.tail_f('testFname')
    #         mock_io.assert_called_once_with(
    #             '/var/syslog/hosts/buffalo.setup/testFname'
    #         )


if __name__ == '__main__':
    unittest.main()
