import requests

url = "https://karaf-g.infarmbureau.com:8443/api/policies/PT%20%20RG%201229641"

headers = {
    'cache-control': "no-cache",
    'postman-token': "3025df6f-09a8-411c-c3e3-be6922bb3b82"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)