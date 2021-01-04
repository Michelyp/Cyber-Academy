import httplib
h = httplib.HTTP('www.cwi.nl')
h.putrequest('GET','/index.html')
h.putheader('Accept','text/html')
h.putheader('Accept','text/plain')
h.endheaders()
errcode,errmsg, headers = h.getreply()
print(errcode)
#debería ser 200
f= h.getfile()
data = f.read()
#obtener el html
f.close()