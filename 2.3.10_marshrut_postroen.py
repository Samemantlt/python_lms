def main():
    x, y = 0, 0
    
    while True:
        direction = input()
        if direction == 'СТОП':
            break

        distance = int(input())
        if direction == 'СЕВЕР':
            y += distance
        if direction == 'ЮГ':
            y -= distance
        if direction == 'ВОСТОК':
            x += distance
        if direction == 'ЗАПАД':
            x -= distance
    
    print(y)
    print(x)


if __name__ == '__main__':
    main()
