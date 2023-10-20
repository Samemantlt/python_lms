def is_in_green_circle(x, y):
    return x ** 2 + y ** 2 <= 100


def is_in_red_area(x, y):
    def para(x):
        return (x + 7) * (x - 5) * 0.25
    
    para_y = para(x)
    if y < para_y:
        return False
    
    def line_1(x):
        return 5 * x / 3 + 35 / 3
    
    line_1_y = line_1(x)
    if y > line_1_y:
        return False
    
    if y > 5:
        return False
    
    if x ** 2 + y ** 2 > 5 ** 2:
        return False
    
    return True


def main():
    x = float(input())
    y = float(input())

    if not is_in_green_circle(x, y):
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    elif not is_in_red_area(x, y):
        print('Зона безопасна. Продолжайте работу.')
    else:
        print('Опасность! Покиньте зону как можно скорее!')


if __name__ == '__main__':
    main()
