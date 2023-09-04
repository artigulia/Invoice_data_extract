import requests
import json

url = "https://ocr.asprise.com/api/v1/receipt"
image = "receipt1.jpeg"

res = requests.post(url,
                    data = {
                        'api_key': 'TEST',
                        'recognizer':'auto',
                        'ref_no':'ocr_python_123'
                    }, files = {
                        'file': open(image,'rb')
                    })


with open("response.json","w") as f:
    json.dump(json.loads(res.text),f)