import requests


address = input()
url = f'http://{address}'


def get_number():
    response = requests.get(url)
    return int(response.text)


result = 0
while True:
    num = get_number()
    if num == 0:
        break
    result += num

print(result)
