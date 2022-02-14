#Get Accounts before
#Get Subnets before

#Add Account - need a loop that does it fior every account
#Add Subnets - needs looking at, how can we add to the end each time?

#Get Accounts after
#Get Subnets after

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {
  'Authorization': 'Bearer 6sxksn568pNkqd6yq84sbmh1zx1w8k',
  'Content-Type': 'text/plain'
}


IP = "18.133.236.75"
base_url = "https://{FortigateIP}/api/v2/cmdb/".format(FortigateIP=IP)

def GetSubnetFilters ():
    get_addresses_url = base_url + "firewall/address/AWSDynamicRule1"

    get_address_response = requests.request("GET", get_addresses_url , headers=headers, verify=False)
#print(get_address_response.text)
#use above if full output required


    data = json.loads(get_address_response.text)
    print('Below are all the subnet filters:')
    print(data['results'][0]['filter'])



def GetAWSAccounts ():
    get_AWS_Accounts_url = base_url + "system/sdn-connector"

    get_address_response = requests.request("GET", get_AWS_Accounts_url , headers=headers, verify=False)
#print(get_address_response.text)
#use above if full output required


    data = json.loads(get_address_response.text)
    print('Below are all the AWS Accounts:')
    print(data['results'][0]['external-account-list'])


def PUTAccounts ():

    PUT_AWS_Accounts_url = base_url + "system/sdn-connector/AWS-Dynamic-Rules"

    Accounts = ["347754476247", "431985927793"]
    for x in Accounts:
        prepayload = {
                    "external-account-list": [
                        {
                            "role-arn": "arn:aws:iam::{}:role/Fortigate-Role-ToBeAssumed".format(x),
                            "region-list": [
                                {
                                    "region": "eu-west-2",
                                }
                            ]
                        }
                    ]
                }



    payload = json.dumps(prepayload)




    response = requests.request("PUT", PUT_AWS_Accounts_url, headers=headers, data=payload, verify=False)

    print('AWS Account Added!')



def PUTSubnets ():

    Subnets = ["SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e"]
    for x in Subnets:
        PUT_AWS_Subnets_URL = base_url + "firewall/address/AWSDynamicRule1"

        prepayload =  {

                    "filter": Subnets
                }

        payload = json.dumps(prepayload)


        response = requests.request("PUT", PUT_AWS_Subnets_URL, headers=headers, data=payload, verify=False)

        print('Subnets Added!')




GetAWSAccounts()
PUTAccounts()
GetAWSAccounts()
GetSubnetFilters()
PUTSubnets()
GetSubnetFilters()





    