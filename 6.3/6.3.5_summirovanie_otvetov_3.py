import requests
import sys


address = input()

paths = sys.stdin.read().splitlines()

result = 0

for path in paths:
    if path is None or path == '':
        continue

    url = f'http://{address}{path}'
    response = requests.get(url)
    nums = response.json()
    result += sum(nums)

print(result)
