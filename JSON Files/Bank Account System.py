#Program:A bank stores customer account information in a JSON file.
import json

account = {
    "account_number": 456789,
    "holder": "Aneela",
    "balance": 125000,
    "account_type": "Savings"
}

with open("account.json","w") as file:
    json.dump(account,file,indent=4)

with open("account.json","r") as file:
    account = json.load(file)

print(f"Account Number:{account['account_number']}")
print(f"Account Holder:{account['holder']}")
print(f"Current Balance:{account['balance']}")
print(f"Account Type:{account['account_type']}")
if(account["balance"]>=100000):
    print("Premium Customer")
else:
    print("Regular Customer")    

if(account["account_type"].lower()=="savings"):
    print("Eligible for Savings Interest")
else:
    print("Interest benefits not available")

print(type(account))