import requests
import json

url="http://www.boredapi.com/api/activity/"
response = requests.get(url)
activity = json.loads(response.text)["activity"]
print('Aktivite: ' + activity)



