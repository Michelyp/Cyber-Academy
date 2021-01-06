import urllib.request

proxies = {'http': 'http://<ip_address>:<Port>'}
print("Using HTTP proxy %s" % proxies['http'])
response = urllib.request.urlopen("http://www.google.com", proxies=proxies)
response.geturl()
response.getcode()
response.headers.keys()
response.headers.values()
for header, value in response.headers.items():
    print(header + ":" + value)