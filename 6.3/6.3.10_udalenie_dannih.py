import requests
import sys
import re


address = input()
user_id = int(input())

url = f'http://{address}/users/{user_id}'

response = requests.delete(url)
assert response.ok
