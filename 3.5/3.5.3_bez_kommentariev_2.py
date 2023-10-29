from sys import stdin


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    
    for line in lines:
        if line.lstrip(' ').startswith('#'):
            continue

        uncommented = line.split('#')[0].rstrip(' ')
        print(uncommented)


if __name__ == '__main__':
    main()
