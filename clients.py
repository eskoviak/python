import requests

url = "http://ap-karafa-dev:8181/api/clients/AL5G9FQFF030CLTCTCN2"

headers = {
    'cache-control': "no-cache",
    'postman-token': "7b4e5d22-ff4c-f3f7-3ef1-8749f79d909b"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)