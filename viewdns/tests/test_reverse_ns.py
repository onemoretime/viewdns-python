import unittest
import responses
import viewdns
import json

from .BaseTest import BaseTest

class TestReverseMx(BaseTest):

    def setUp(self):
        
        super(TestReverseMx, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_reverse_ip(self):

        data = self.load_from_file('reverse_ns.json')

        url = self.base_url + 'reversens'
        responses.add(responses.GET, url, body=data, status=200)

        reverse_ns = self.client.reverse_ns('ns1.websitewelcome.com')

        self.assertEqual(reverse_ns.domain_count, '10897')
        self.assertEqual(reverse_ns.total_pages, '2')

        self.assertEqual(reverse_ns.current_page, '1')
        self.assertIsInstance(reverse_ns.domains,list)
        result = set(t for d in reverse_ns.domains for t in d.items())
        target = set(t for d in json.loads(data)['response']['domains'] for t in d.items())
        self.assertTrue(result.issubset(target))
        
