
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
    print('Below are all the subnet filters before running:')
    print(data['results'][0]['filter'])



def GetAWSAccounts ():
    get_AWS_Accounts_url = base_url + "system/sdn-connector"

    get_address_response = requests.request("GET", get_AWS_Accounts_url , headers=headers, verify=False)
#print(get_address_response.text)
#use above if full output required


    data = json.loads(get_address_response.text)
    print('Below are all the AWS Accounts before running:')
    print(data['results'][0]['external-account-list'])


def PUTAccounts ():

    PUT_AWS_Accounts_url = base_url + "system/sdn-connector/AWS-Dynamic-Rules"

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




    response = requests.request("PUT", PUT_AWS_Accounts_url, headers=headers, data=payload, verify=False)

    print('AWS Account Added!')

""" 
def PUTSubnets ():

    PUT_AWS_Subnets_URL = base_url + "firewall/address/AWSDynamicRule1"

    prepayload =  {

                "filter": "SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e"
            }

    payload = json.dumps(prepayload)

    response = requests.request("PUT", PUT_AWS_Subnets_URL, headers=headers, data=payload, verify=False)

    print(response.text) """


def POSTDynamicAddress ():

    POST_Dynamic_Address_URL = base_url + "firewall/address"

    prepayload =  {
    
            "name": "AWSDynamicRule2",
            "type": "dynamic",
            "sub-type": "sdn",
            "sdn": "AWS-Dynamic-Rules",
            "interface": "",
            "filter": "SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e",
    }

    payload = json.dumps(prepayload)

    response = requests.request("POST",  POST_Dynamic_Address_URL, headers=headers, data=payload, verify=False)

    #print(response.text)
    #data = json.loads(response.text)
    #print(data['mkey'])


def PUTRootAddrGrp ():

    PUT_Root_AddrGrp_URL = base_url + "firewall/addrgrp/Dynamic-Addrgrp"

    prepayload =  {
            "member": [
                {
                    "name": "AWSDynamicRule1",
                },
                {
                    "name": "AWSDynamicRule2",
                }
            ],
        }


    payload = json.dumps(prepayload)

    response = requests.request("PUT",  PUT_Root_AddrGrp_URL, headers=headers, data=payload, verify=False)

    print(response.text)


GetSubnetFilters()
GetAWSAccounts()
PUTAccounts()
GetAWSAccounts()
POSTDynamicAddress()
PUTRootAddrGrp()





    