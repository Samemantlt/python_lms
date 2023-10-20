def main():
    result = 0

    for _ in range(int(input())):
        text = input()

        result += text.count('зайка')
    
    print(result)


if __name__ == '__main__':
    main()
