import requests


address = input()
url = f'http://{address}/users'

response = requests.get(url)
users = response.json()

names = [f'{user["last_name"]} {user["first_name"]}' for user in users]
names = sorted(names)

for name in names:
    print(name)
