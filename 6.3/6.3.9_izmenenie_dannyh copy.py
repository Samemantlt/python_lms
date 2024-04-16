import requests
import sys
import re


address = input()
user_id = int(input())

change_lines = sys.stdin.read().splitlines()
body = dict()

for line in change_lines:
    if line is None or line == '':
        continue
    match = re.fullmatch("(?P<field>[^=]+)=(?P<value>.*)", line)

    field = match.group('field')
    value = match.group('value')

    body[field] = value

url = f'http://{address}/users/{user_id}'

response = requests.put(url, json=body)
assert response.ok
