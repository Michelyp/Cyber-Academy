import urllib2
response = urllib2.urlopen("dominio")
response.geturl()
response.getcode()
response.headers.keys()
response.headers.values()
for header, value in response.headers.items():
    print(header + ":"+value)
auth = urllib2.HTTPBasicAuthHandler()
auth.add_password(user="guest",password="passwd",url="dominio")
