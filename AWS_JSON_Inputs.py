
Accounts_prepayload = {
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


Account_Subnet_Filters = [
    {
    
            "name": "Account1-private",
            "type": "dynamic",
            "sub-type": "sdn",
            "sdn": "AWS-Dynamic-Rules",
            "interface": "",
            "filter": "SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e",
    },
    {
    
            "name": "Account1-public",
            "type": "dynamic",
            "sub-type": "sdn",
            "sdn": "AWS-Dynamic-Rules",
            "interface": "",
            "filter": "SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e",
    },
    {
    
            "name": "Account2-private",
            "type": "dynamic",
            "sub-type": "sdn",
            "sdn": "AWS-Dynamic-Rules",
            "interface": "",
            "filter": "SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e",
    },
    {
    
            "name": "Account2-public",
            "type": "dynamic",
            "sub-type": "sdn",
            "sdn": "AWS-Dynamic-Rules",
            "interface": "",
            "filter": "SubnetId=subnet-7653131f | SubnetId=subnet-0c223b152937d018f | SubnetId=subnet-0b51741dc095e467e",
    }
]


Private_Addrgrp_members_Private = {
            "member": [
                {
                    "name": "Account1-private",
                },
                {
                    "name": "Account2-private",
                }
            ],
        }


Private_Addrgrp_members_Public = {
            "member": [
                {
                    "name": "Account1-public",
                },
                {
                    "name": "Account2-public",
                }
            ],
        }