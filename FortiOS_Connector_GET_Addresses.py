import requests
import json

IP = "18.133.236.75"

url = "https://{FortigateIP}/api/v2/cmdb/firewall/address".format(FortigateIP=IP)

payload={}
headers = {
  'Authorization': 'Bearer 6sxksn568pNkqd6yq84sbmh1zx1w8k'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

data = json.loads(response.text)
print('Below are all the addesses:')
print(data['results'][0]['name'])


