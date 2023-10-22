import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestIpHistory(BaseTest):

    def setUp(self):
        
        super(TestIpHistory, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_ip_history(self):

        data = self.load_from_file('ip_history.json')

        url = self.base_url + 'iphistory'
        responses.add(responses.GET, url, body=data, status=200)

        ip_records = self.client.get_ip_history('example.com')

        self.assertEqual(ip_records[0].ip, '93.184.216.34')
        self.assertEqual(ip_records[0].location, 'United States')
        self.assertEqual(ip_records[0].owner, 'NETBLK-03-EU-93-184-216-0-24')
        self.assertEqual(ip_records[0].lastseen, '2016-09-13')

        self.assertEqual(ip_records[1].ip, '93.184.216.119')
        self.assertEqual(ip_records[1].location, 'United States')
        self.assertEqual(ip_records[1].owner, 'NETBLK-03-EU-93-184-216-0-24')
        self.assertEqual(ip_records[1].lastseen, '2014-12-09')

        self.assertEqual(ip_records[2].ip, '192.0.43.10')
        self.assertEqual(ip_records[2].location, 'Los Angeles - United States')
        self.assertEqual(ip_records[2].owner, 'ICANN')
        self.assertEqual(ip_records[2].lastseen, '2013-07-09')

        self.assertEqual(ip_records[3].ip, '192.0.32.10')
        self.assertEqual(ip_records[3].location, 'Los Angeles - United States')
        self.assertEqual(ip_records[3].owner, 'ICANN')
        self.assertEqual(ip_records[3].lastseen, '2011-06-05')        

