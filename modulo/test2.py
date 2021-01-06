import httplib2
h = httplib2.Http()
response = h.request('dominio',"GET")
response.geturl()
response.getcode()
response.headers.keys()
response.headers.values()
for header,value in response.headers.items():
	print (header + ":" + value)