import requests


address = input()
response = requests.get(f'http://{address}')

numbers = response.json()
result = 0
for el in numbers:
    if isinstance(el, int) or isinstance(el, float):
        result += el

print(result)
