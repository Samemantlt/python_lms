from sys import stdin
import json


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))

    filename = lines[0]
    vals = {key: value for key, value in [line.split(' == ') for line in lines[1:]]}

    with open(filename) as file:
        obj = json.load(file)
    
    for key, val in vals.items():
        obj[key] = val
    
    with open(filename, 'w') as file:
        json.dump(obj, file)


if __name__ == '__main__':
    main()
