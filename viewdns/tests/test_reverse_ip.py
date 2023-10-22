import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestReverseIp(BaseTest):

    def setUp(self):
        
        super(TestReverseIp, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_reverse_ip(self):

        data = self.load_from_file('reverse_ip.json')

        url = self.base_url + 'reverseip'
        responses.add(responses.GET, url, body=data, status=200)

        reverse_ips = self.client.reverse_ip('199.59.148.10')

        self.assertEqual(reverse_ips[0].name, 'gezwitscher.com')
        self.assertEqual(reverse_ips[0].last_resolved, '2011-04-04')

        self.assertEqual(reverse_ips[1].name, 'twitter.com')
        self.assertEqual(reverse_ips[1].last_resolved, '2011-04-04')

        self.assertEqual(reverse_ips[2].name, 'twitterfriendblaster.com')
        self.assertEqual(reverse_ips[2].last_resolved, '2012-01-11')

        self.assertEqual(reverse_ips[3].name, 'twttr.com')
        self.assertEqual(reverse_ips[3].last_resolved, '2012-02-21')
