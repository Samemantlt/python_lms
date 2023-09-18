def main():
    item_name = input()
    price_per_one = int(input())
    amount = int(input())
    payed = int(input())


    total_price = price_per_one * amount
    charge = payed - total_price

    print(f"""Чек
    {item_name} - {amount}кг - {price_per_one}руб/кг
    Итого: {total_price}руб
    Внесено: {payed}руб
    Сдача: {charge}руб
    """)


if __name__ == '__main__':
    main()
