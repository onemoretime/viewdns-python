import requests

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse

from .DNSRecord import DNSRecord
from .HTTPHeader import HTTPHeader
from .IPLocation import IPLocation
from .FreeEmail import FreeEmail
from .IpHistory import IpHistory
from .MacLookup import MacLookup
from .Ping import Ping
from .PortScanner import PortScanner
from .ReverseDns import ReverseDns
from .ReverseIp import ReverseIp
from .ReverseMx import ReverseMx
from .ReverseNs import ReverseNs
from .Balance import Balance

class Client():

    base_url = 'https://api.viewdns.info/'
    api_key = None

    def __init__(self, api_key):
        """
        Creates a new instance of the ViewDNS.info API client.

        The ViewDNS.info API allows webmasters to integrate the tools provided by ViewDNS.info into their own sites in a simple and effective manner.

        Docs: https://viewdns.info/api/docs/
        """

        self.api_key = api_key

    def get_ip_history(self, domain):
        """
        Shows a historical list of IP addresses a given domain name has been hosted on 
        as well as where that IP address is geographically located, 
        and the owner of that IP address.

        Params:

        * domain -  the domain to find historical IP addresses for

        Docs: https://viewdns.info/api/docs/ip-history.php
        """

        params = dict()
        params['domain'] = domain
    

        res = self._execute('iphistory', params=params)

        ip_records = []

        for ip_record in res['response']['records']:
            # class is a reserved word :|            
            ip_record = IpHistory(**ip_record)
            ip_records.append(ip_record)

        return ip_records

    def port_scanner(self, host):
        """
        This web based port scanner will test whether common ports are open on a server.
        Useful in determining if a specific service (e.g. HTTP) is up or down on a specific server. 

        Ports scanned are: 21, 22, 23, 25, 80, 110, 139, 143, 445, 1433, 1521, 3306 and 3389

        Params:

        * host - the host to perform the port scanner on (domain or IP address)

        Docs: https://viewdns.info/api/docs/port-scanner.php
        """

        params = dict()
        params['host'] = host

        res = self._execute('portscan', params=params)

        ports = []

        for port in res['response']['port']:
            port = PortScanner(**port)
            ports.append(port)

        return ports

    def reverse_ns(self, ns, page=None):
        """
        Takes a mail server (e.g. mail.google.com) and quickly shows 
        all other domains that use the same mail server.
        Useful for identifying domains that are used as email aliases

        Params:

        * ns - the nameserver to query

        * page - view further pages of results (e.g. '2' to view results 10,001 to 20,000) - optional

        todo: use page param

        Docs: https://viewdns.info/api/docs/reverse-ns-lookup.php
        """

        params = dict()
        params['ns'] = ns

        res = self._execute('reversens', params=params)

        reverse_ns = ReverseNs(**res['response'])

        return reverse_ns

    def reverse_mx(self, mx, page=None):
        """
        Takes a mail server (e.g. mail.google.com) and quickly shows 
        all other domains that use the same mail server.
        Useful for identifying domains that are used as email aliases

        Params:

        * mx - the mail server to query

        * page - view further pages of results (e.g. '2' to view results 10,001 to 20,000) - optional

        todo: use page param

        Docs: https://viewdns.info/api/docs/reverse-mx-lookup.php
        """

        params = dict()
        params['mx'] = mx

        res = self._execute('reversemx', params=params)

        reverse_mx = ReverseMx(**res['response'])

        return reverse_mx

    def reverse_ip(self, host, page=None):
        """
        View all configured DNS records (A, MX, CNAME etc.) for a specified domain name.

        Params:

        * host - the domain or IP address to find all hosted domains on

        * page - view further pages of results (e.g. '2' to view results 10,001 to 20,000) - optional

        todo: use page param

        Docs: https://viewdns.info/api/docs/reverse-ip-lookup.php
        """

        params = dict()
        params['host'] = host

        res = self._execute('reverseip', params=params)

        domains = []

        for domain in res['response']['domains']:        
            domain = ReverseIp(**domain)
            domains.append(domain)

        return domains

    def get_dns_records(self, domain, record_type='ANY'):
        """
        View all configured DNS records (A, MX, CNAME etc.) for a specified domain name.

        Params:

        * domain - the domain name to lookup DNS records for

        * recordtype - the type of DNS record you wish to retrieve (default 'ANY')

        Docs: https://viewdns.info/api/docs/dns-record-lookup.php
        """

        params = dict()
        params['domain'] = domain
        params['recordtype'] = record_type

        res = self._execute('dnsrecord', params=params)

        dns_records = []

        for dns_record in res['response']['records']:
            # class is a reserved word :|
            dns_record['class_'] = dns_record['class']
            dns_record = DNSRecord(**dns_record)
            dns_records.append(dns_record)

        return dns_records
    
    def get_http_headers(self, domain):
        """
        Retrieves the HTTP headers of a remote domain. Useful in determining the web server (and version) in use and much more.

        Params:

        * domain - the domain to retrieve the HTTP headers for

        Docs: https://viewdns.info/api/docs/get-http-headers.php
        """

        params = dict()
        params['domain'] = domain

        res = self._execute('httpheaders', params=params)

        http_headers = []

        for http_header in res['response']['headers']:
            http_header = HTTPHeader(**http_header)
            http_headers.append(http_header)

        return http_headers

    def ping(self, host):
        """
        Test how long a response from remote system takes to reach the ViewDNS server. Useful for detecting latency issues on network connections.

        Params:

        * host - the domain or IP address to perform a ping on

        Docs: https://viewdns.info/api/docs/ping.php
        """

        params = dict()
        params['host'] = host

        res = self._execute('ping', params=params)

        rtts = []

        for rtt in res['response']['replys']:
            rtt = Ping(**rtt)
            rtts.append(rtt)

        return rtts    

    def get_free_email_lookup(self, domain):
        """
        This tool will find out if a domain name provides free email addresses.
        Search is performed on a custom made list of thousands of known free email hosts.
        
        Params:

        * domain - the domain name to test for free email services

        Docs: https://viewdns.info/api/docs/free-email-lookup.php
        """

        params = dict()
        params['domain'] = domain

        res = self._execute('freeemail', params=params)

        provide_free_email = FreeEmail(**res['response'])

        return provide_free_email

    def reverse_dns(self, ip):
        """
        Find the reverse DNS entry (PTR) for a given IP. This is generally the server or host name.
        
        Params:

        * ip - the IP address to retrieve the reverse DNS record for

        Docs: https://viewdns.info/api/docs/reverse-dns-lookup.php
        """

        params = dict()
        params['ip'] = ip

        res = self._execute('reversedns', params=params)

        rdns = ReverseDns(**res['response'])

        return rdns

    def get_ip_location(self, ip):
        """
        This tool will display geographic information about a supplied IP address including city, country, latitude, longitude and more.
        
        Params:

        * ip - the ip address to find the location of

        Docs: https://viewdns.info/api/docs/ip-location-finder.php
        """

        params = dict()
        params['ip'] = ip

        res = self._execute('iplocation', params=params)

        ip_location = IPLocation(**res['response'])

        return ip_location

    def mac_lookup(self, mac):
        """
        This tool will display the name of the company that manufactured a specific network device based on its MAC Address.
        
        Params:

        * mac - the MAC address to lookup

        Docs: https://viewdns.info/api/docs/mac-address-lookup.php
        """

        params = dict()
        params['mac'] = mac

        res = self._execute('maclookup', params=params)

        mac_lookup = MacLookup(**res['response'])

        return mac_lookup

    def balance(self):
        """
        View the current query count, limit and balance of any prepaid queries for your API account.    

        Docs: https://viewdns.info/api/docs/account-balance.php
        """

        params = dict()
        params['action'] = 'balance'

        res = self._execute(None, params=params)

        balance = Balance(**res['response'])

        return balance    

    def _execute(self, url = None, params=None):
        computed_url = self.base_url
        if url:
            computed_url = urlparse.urljoin(self.base_url, url)

        if params is None:
            params = dict()

        params['apikey'] = self.api_key
        params['output'] = 'json'

        req = requests.get(computed_url, params=params)

        if req.status_code == 404:
            raise Exception()

        try:
            data = req.json()
        except ValueError as e:
            raise Exception(e)

        return data
