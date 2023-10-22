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

        data = self.load_from_file('ping.json')

        url = self.base_url + 'ping'
        responses.add(responses.GET, url, body=data, status=200)

        rtts = self.client.ping('twitter.com')

        self.assertEqual(rtts[0].rtt, "32.5 ms")

        self.assertEqual(rtts[1].rtt, "36.2 ms")

        self.assertEqual(rtts[2].rtt, "30.8 ms")

        self.assertEqual(rtts[3].rtt, "36.6 ms")       

