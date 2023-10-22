import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestIpLocation(BaseTest):

    def setUp(self):
        
        super(TestIpLocation, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_get_free_email_lookup(self):

        
        url = self.base_url + 'freeemail'

        data = self.load_from_file('free_email_lookup_false.json')
        responses.add(responses.GET, url, body=data, status=200)
        provide_free_email = self.client.get_free_email_lookup('test.com')
        print(provide_free_email)
        self.assertFalse(provide_free_email.provide_free_email)

        data = self.load_from_file('free_email_lookup_true.json')
        responses.add(responses.GET, url, body=data, status=200)
        provide_free_email = self.client.get_free_email_lookup('gmail.com')
        self.assertTrue(provide_free_email.provide_free_email)        
