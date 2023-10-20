def main():
    for _ in range(int(input())):
        text = input()
        index = text.find('зайка')
        if index == -1:
            print('Заек нет =(')
        else:
            print(index + 1)


if __name__ == '__main__':
    main()
