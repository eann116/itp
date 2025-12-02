import json
import urllib.request  

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)

# Read raw bytes, decode JSON into Python structures
result = json.loads(response.read())

print(result)

with open("iss.txt", "w") as file:
    file.write(f"There are currently {result['number']} astronauts on the ISS:\n\n")
    for person in result["people"]:
        file.write(person["name"] + " - onboard\n")