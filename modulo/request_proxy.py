import urllib3

pool = urllib3.PoolManager(10)

dirección_proxy = "http://<ip_dirección>:<puerto>"
proxy = urllib3.ProxyManager(proxy_address)
response = proxy.request('GET', 'http://www.google.com')
print(response.status)
response.headers.keys()
response.headers.values()
for header, value in response.headers.items():
    print(header + ":" + value)
