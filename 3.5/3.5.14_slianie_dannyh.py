from sys import stdin
import json


def main():
    filename = input()
    with open(filename) as file:
        users: list = json.load(file)
    
    filename2 = input()
    with open(filename2) as file:
        updates = json.load(file)

    for update in updates:
        user = next(filter(lambda a: a['name'] == update['name'], users))
        for prop in update:
            if prop == 'name':
                continue
            if prop in user:
                user[prop] = max(user[prop], update[prop])
            else:
                user[prop] = update[prop]
    
    result = dict()
    for user in users:
        user_result = dict()
        name = user['name']

        for prop in user:
            if prop == 'name':
                continue

            user_result[prop] = user[prop]
        
        result[name] = user_result
    
    with open(filename, 'w') as file:
        json.dump(result, file)


if __name__ == '__main__':
    main()
