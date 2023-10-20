import math


def main():
    number = 500
    step = 250

    print(number)
    while (answer := input()) != 'Угадал!':
        if answer == 'Меньше':
            number -= step
        if answer == 'Больше':
            number += step
        
        print(number)
        step = int(math.ceil(step / 2))


if __name__ == '__main__':
    main()
