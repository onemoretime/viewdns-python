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

        data = self.load_from_file('reverse_mx.json')

        url = self.base_url + 'reversemx'
        responses.add(responses.GET, url, body=data, status=200)

        reverse_mx = self.client.reverse_mx('mail.google.com')

        self.assertEqual(reverse_mx.domain_count, '818')
        self.assertEqual(reverse_mx.total_pages, '1')

        self.assertEqual(reverse_mx.current_page, '1')
        self.assertIsInstance(reverse_mx.domains,list)
        self.assertTrue(set(reverse_mx.domains).issubset(set(json.loads(data)['response']['domains'])))
        
