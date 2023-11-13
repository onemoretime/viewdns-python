import unittest
import responses
import viewdns
import json

from .BaseTest import BaseTest

class TestBalance(BaseTest):

    def setUp(self):
        
        super(TestBalance, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_balace(self):

        data = self.load_from_file('balance.json')

        url = self.base_url + 'account'
        responses.add(responses.GET, url, body=data, status=200)

        balance = self.client.balance()

        self.assertEqual(balance.limit, 250)
        self.assertEqual(balance.usage, 123)
        self.assertEqual(balance.balance, 0)
        self.assertFalse(balance.warning)

        warning_data_dict = json.loads(data)
        warning_data_dict['response']['monthly']['usage'] = '200'
        warning_data = json.dumps(warning_data_dict)
        responses.add(responses.GET, url, body=warning_data, status=200)
        balance = self.client.balance()
        self.assertTrue(balance.warning)

        