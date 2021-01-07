import requests, json

print("Requests probando API REST")
response = requests.get("http://httpbin.org/get?id=0123456789",timeout=5)
print("Status code: " + str(response.status_code))
if response.status_code == 200:
    results = response.json()
for result in results.items():
    print(result)
    print("Headers response: ")
for header, value in response.headers.items():
    print(header, '-->', value)
    print("Headers request : ")
for header, value in response.request.headers.items():
    print(header, '-->', value)
    print("Server:" + response.headers['server'])
else:
    print("Error code %s" % response.status_code)
