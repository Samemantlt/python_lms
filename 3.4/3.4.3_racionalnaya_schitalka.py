def main():
    start, end, step = map(float, input().split())
    
    current = start
    while current <= end:
        print(current)
        current += step


if __name__ == '__main__':
    main()
