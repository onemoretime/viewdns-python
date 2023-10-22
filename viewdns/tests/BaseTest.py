import os
import unittest
import secrets

class BaseTest(unittest.TestCase):

    def setUp(self):

        self.base_url = 'https://api.viewdns.info/'
        # random token
        self.api_token = secrets.token_hex(16)

    def load_from_file(self, json_file):

        cwd = os.path.dirname(__file__)

        with open(os.path.join(cwd, 'data/%s' % json_file), 'r') as f:
            return f.read()
