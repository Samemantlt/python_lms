def get_cos_angle_sign(a, b, c):
    return - a ** 2 + b ** 2 + c ** 2


def main():
    # a ** 2 = b ** 2 + c ** 2 - 2 * b * c * cos(alpha)
    # a ** 2 - b ** 2 - c ** 2 = - 2 * b * c * cos(alpha)
    # - a ** 2 + b ** 2 + c ** 2 = 2 * b * c * cos(alpha)

    a = int(input())
    b = int(input())
    c = int(input())

    a_cos_sign = get_cos_angle_sign(a, b, c)
    c_cos_sign = get_cos_angle_sign(c, a, b)
    b_cos_sign = get_cos_angle_sign(b, c, a)

    min_cos = min(a_cos_sign, b_cos_sign, c_cos_sign)
    
    if min_cos > 0:
        print('крайне мала')
    elif min_cos == 0:
        print('100%')
    else:
        print('велика')


if __name__ == '__main__':
    main()
