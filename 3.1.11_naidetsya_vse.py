def main():
    lines = []
    
    for _ in range(int(input())):
        lines.append(input())
    
    query = input()

    for line in lines:
        if query.lower() in line.lower():
            print(line)


if __name__ == '__main__':
    main()
