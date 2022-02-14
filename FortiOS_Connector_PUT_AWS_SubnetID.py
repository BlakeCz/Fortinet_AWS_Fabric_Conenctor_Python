import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IP = "18.133.236.75"

url = "https://{FortigateIP}/api/v2/cmdb/firewall/address/AWSDynamicRule1".format(FortigateIP=IP)

prepayload =  {

            "filter": "SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e"
        }

payload = json.dumps(prepayload)


headers = {
  'Authorization': 'Bearer 6sxksn568pNkqd6yq84sbmh1zx1w8k',
  'Content-Type': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

print(response.text)