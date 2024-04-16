import requests


address = input()
request = {
    'username': input(),
    'last_name': input(),
    'first_name': input(),
    'email': input()
}

url = f'http://{address}/users'

response = requests.post(url, json=request)
assert response.ok
