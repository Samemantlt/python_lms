import requests
import sys


address = input()
user_id = int(input())
message = sys.stdin.read()

url = f'http://{address}/users/{user_id}'

response = requests.get(url)

if not response.ok:
    print('Пользователь не найден')
    sys.exit(0)

user: dict = response.json()

message = message.format(
    email=user['email'],
    last_name=user['last_name'],
    first_name=user['first_name'],
    username=user['username'],
    id=user['id'],
)

print(message)
