import requests

url = "https://api-id.execute-api.region.amazonaws.com/stage"
payload = {"sensor_data" : data}
headers + {"Content-Type":"application/json"}

respinse = requests.post(url, json=payload , headers=headers)
print(response.status_code, response.text)
