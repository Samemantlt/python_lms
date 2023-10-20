from sys import stdin


def main():
    lines = []

    for line in stdin:
        line = line.strip()
        if line is None or line == '':
            break
        
        lines.append(line.strip())

    objects_map = dict()

    for line in lines:
        words = line.split(' ')
        for word in words:
            if word not in objects_map:
                objects_map[word] = 0
            
            objects_map[word] += 1

    for key, value in objects_map.items():
        print(f'{key} {value}')


if __name__ == '__main__':
    main()
