def main():
    filename = input()
    lines_count = int(input())

    with open(filename) as file:
        text = file.read()
    
    lines = text.splitlines()

    for line in lines[-lines_count:]:
        print(line)


if __name__ == '__main__':
    main()
