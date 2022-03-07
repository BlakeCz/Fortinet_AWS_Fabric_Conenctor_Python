
import requests
import json
import urllib3
from AWS_JSON_Inputs import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {
  'Authorization': 'Bearer 6sxksn568pNkqd6yq84sbmh1zx1w8k',
  'Content-Type': 'text/plain'
}


IP = "18.168.152.167"
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

    prepayload = Accounts_prepayload 
    # Accounts_prepayload taken from Inputs file

    payload = json.dumps(prepayload)




    response = requests.request("PUT", PUT_AWS_Accounts_url, headers=headers, data=payload, verify=False)

    print('AWS Account Added!')




def POSTDynamicAddress ():

    POST_Dynamic_Address_URL = base_url + "firewall/address"

    for Firewall_Address in Account_Subnet_Filters:
        prepayload =  Firewall_Address

        payload = json.dumps(prepayload)

        response = requests.request("POST",  POST_Dynamic_Address_URL, headers=headers, data=payload, verify=False)

        #print(response.text)
        #data = json.loads(response.text)
        #print(data['mkey'])


def PUTRootAddrGrpPrivate ():

    PUT_Root_AddrGrp_URL = base_url + "firewall/addrgrp/Dynamic-Addrgrp-Private"

    prepayload =  Private_Addrgrp_members_Private


    payload = json.dumps(prepayload)

    response = requests.request("PUT",  PUT_Root_AddrGrp_URL, headers=headers, data=payload, verify=False)

    print(response.text)


def PUTRootAddrGrpPublic ():

    PUT_Root_AddrGrp_URL = base_url + "firewall/addrgrp/Dynamic-Addrgrp-Public"

    prepayload =  Private_Addrgrp_members_Public

    payload = json.dumps(prepayload)

    response = requests.request("PUT",  PUT_Root_AddrGrp_URL, headers=headers, data=payload, verify=False)

    print(response.text)


GetSubnetFilters()
GetAWSAccounts()
PUTAccounts()
GetAWSAccounts()
POSTDynamicAddress()
PUTRootAddrGrpPrivate()
PUTRootAddrGrpPublic()





    