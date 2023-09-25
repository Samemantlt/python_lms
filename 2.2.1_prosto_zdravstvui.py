def main():
    print('Как Вас зовут?')
    username = input()

    print(f'Здравствуйте, {username}!')
    print('Как дела?')

    feeling = input()

    if feeling == 'хорошо':
        print('Я за вас рада!')
    elif feeling == 'плохо':
        print('Всё наладится!')


if __name__ == '__main__':
    main()
