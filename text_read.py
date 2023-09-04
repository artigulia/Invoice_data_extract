import json
import requests

with open("response.json","r") as f:
    data = json.load(f)

print(data.keys())
print(data['receipts'])

print(data['receipts'][0].keys())

items = data['receipts'][0]['items']
print(f"Your purchase at {data['receipts'][0]['merchant_name']}")

for item in items:
    print(f"{item['description']} = {data['receipts'][0]['currency']} {item['amount']}")

# print("-" * 30)
# print(f"Subtotal : {data['receipts'][0]['currency']} {data['receipts'][0]['subtotal']}")
# print(f"Tax : {data['receipts'][0]['currency']} {data['receipts'][0]['tax']}")
# print("-" * 30)
print(f"Total : {data['receipts'][0]['currency']} {data['receipts'][0]['total']}")

