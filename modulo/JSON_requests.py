import requests
print("Requests testin JSON")
response = requests.get("http://api.openweathermap.org/data/2.5/weather?&q=london&appid=0888d6d73eeb6588a5b5da08f4d32bb9",timeout=5)
print("Status code: "+str(response.status_code))
if response.status_code == 200:
    results = response.json()

    for result in results.items():
        print(result)

        print("Headers response: ")
        for header, value in response.headers.items():
            print((header, '-->', value))
            print("Headers request :")
        for header, value in response.request.headers.items():
            print((header,'-->', value))
        else:
            print("Error code %s" %response.status_code)