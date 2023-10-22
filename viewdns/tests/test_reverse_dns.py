import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestReverseDns(BaseTest):

    def setUp(self):
        
        super(TestReverseDns, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_reverse_dns(self):

        data = self.load_from_file('reverse_dns.json')

        url = self.base_url + 'reversedns'
        responses.add(responses.GET, url, body=data, status=200)

        rdns = self.client.reverse_dns('199.59.148.10')

        self.assertEqual(rdns.rdns, "r-199-59-148-10.twttr.com")
    

