def main():
    name = input()
    price = int(input())
    weight = int(input())
    payed = int(input())
    
    print(f"""================Чек================
Товар:{name:>29}
Цена:{f"{weight}кг * {price}руб/кг":>30}
Итого:{price * weight:>26}руб
Внесено:{payed:>24}руб
Сдача:{payed - price * weight:>26}руб
===================================
""")


if __name__ == '__main__':
    main()
