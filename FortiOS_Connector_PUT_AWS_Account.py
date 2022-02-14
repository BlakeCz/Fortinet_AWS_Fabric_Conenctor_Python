import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IP = "18.133.236.75"

url = "https://{FortigateIP}/api/v2/cmdb/system/sdn-connector/AWS-Dynamic-Rules".format(FortigateIP=IP)

prepayload = {
            "external-account-list": [
                {
                    "role-arn": "arn:aws:iam::347754476247:role/Fortigate-Role-ToBeAssumed",
                    "region-list": [
                        {
                            "region": "eu-west-2",
                        }
                    ]
                },
                                {
                    "role-arn": "arn:aws:iam::431985927793:role/Fortigate-Role-ToBeAssumed",
                    "region-list": [
                        {
                            "region": "eu-west-2",
                        }
                    ]
                }
            ],
        }

payload = json.dumps(prepayload)


headers = {
  'Authorization': 'Bearer 6sxksn568pNkqd6yq84sbmh1zx1w8k',
  'Content-Type': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

print(response.text)
#Would need to do a GET before and after to compare, using json laods