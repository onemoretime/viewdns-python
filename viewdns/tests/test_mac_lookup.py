import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestMacLookup(BaseTest):

    def setUp(self):
        
        super(TestMacLookup, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_maclookup(self):

        data = self.load_from_file('maclookup.json')

        url = self.base_url + 'maclookup'
        responses.add(responses.GET, url, body=data, status=200)

        ip_location = self.client.mac_lookup('00-05-02-34-56-78')

        self.assertEqual(ip_location.manufacturer, "APPLE COMPUTER - 20650 VALLEY GREEN DRIVE - CUPERTINO CA 95014 - UNITED STATES")

