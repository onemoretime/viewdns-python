import unittest
import responses
import viewdns

from .BaseTest import BaseTest

class TestPortScanner(BaseTest):

    def setUp(self):
        
        super(TestPortScanner, self).setUp()
        self.client = viewdns.Client(self.api_token)

    @responses.activate
    def test_port_scanner(self):

        data = self.load_from_file('port_scanner.json')

        url = self.base_url + 'portscan'
        responses.add(responses.GET, url, body=data, status=200)

        ports = self.client.port_scanner('viewdns.info')

        self.assertEqual(ports[0].number, '21')
        self.assertEqual(ports[0].service, 'FTP')
        self.assertEqual(ports[0].status, 'closed')

        self.assertEqual(ports[1].number, '22')
        self.assertEqual(ports[1].service, 'SSH')
        self.assertEqual(ports[1].status, 'closed')

        self.assertEqual(ports[2].number, '23')
        self.assertEqual(ports[2].service, 'Telnet')
        self.assertEqual(ports[2].status, 'closed')
        
        self.assertEqual(ports[3].number, '25')
        self.assertEqual(ports[3].service, 'SMTP')
        self.assertEqual(ports[3].status, 'closed')
        
        self.assertEqual(ports[4].number, '80')
        self.assertEqual(ports[4].service, 'HTTP')
        self.assertEqual(ports[4].status, 'open')
        
        self.assertEqual(ports[5].number, '110')
        self.assertEqual(ports[5].service, 'POP3')
        self.assertEqual(ports[5].status, 'closed')
        
        self.assertEqual(ports[6].number, '139')
        self.assertEqual(ports[6].service, 'NETBIOS')
        self.assertEqual(ports[6].status, 'closed')
        
        self.assertEqual(ports[7].number, '143')
        self.assertEqual(ports[7].service, 'IMAP')
        self.assertEqual(ports[7].status, 'closed')
        
        self.assertEqual(ports[8].number, '443')
        self.assertEqual(ports[8].service, 'HTTPS')
        self.assertEqual(ports[8].status, 'closed')
        
        self.assertEqual(ports[9].number, '445')
        self.assertEqual(ports[9].service, 'SMB')
        self.assertEqual(ports[9].status, 'closed')
        
        self.assertEqual(ports[10].number, '1433')
        self.assertEqual(ports[10].service, 'MSSQL')
        self.assertEqual(ports[10].status, 'closed')
        
        self.assertEqual(ports[11].number, '1521')
        self.assertEqual(ports[11].service, 'ORACLE')
        self.assertEqual(ports[11].status, 'closed')
        
        self.assertEqual(ports[12].number, '3306')
        self.assertEqual(ports[12].service, 'MySQL')
        self.assertEqual(ports[12].status, 'closed')
                
        self.assertEqual(ports[13].number, '3389')
        self.assertEqual(ports[13].service, 'Remote Desktop')
        self.assertEqual(ports[13].status, 'closed')
