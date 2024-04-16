import requests


address = input()
key = input()
url = f'http://{address}'

response = requests.get(url)

dictionary = response.json()

result = dictionary.get(key, 'No data')
print(result)
