def main():
    all_weight = int(input())
    all_price = int(input())

    first_price = int(input())
    second_price = int(input())

    """

    first_wight + sec_weight = all_weight
    first_weight * first_price + sec_wigth * sec_price = all_weight * all_price
    
    first_weight = all_weight - sec_weight
    first_weight * first_price + sec_wigth * sec_price = all_weight * all_price

    (all_weight - sec_weight) * first_price + sec_weight * sec_price = all_weight * all_price

    all_weight * first_price - sec_weight * first_price + sec_weight * sec_price = all_weight * all_price

    -sec_weight * first_price + sec_weight * sec_price = all_weight * all_price - all_weight * first_price

    sec_weight * (-first_price + sec_price) = all_weight * all_price - all_weight * first_price

    sec_weight = (all_weight * all_price - all_weight * first_price) / (sec_price - first_price)

    """

    second_weight = (all_weight * all_price - all_weight *
                     first_price) / (second_price - first_price)
    first_weight = all_weight - second_weight

    print(f'{int(first_weight)} {int(second_weight)}')


if __name__ == '__main__':
    main()
