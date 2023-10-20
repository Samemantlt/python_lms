def main():
    price_per_one = int(input())
    amount = int(input())
    payed = int(input())


    total_price = price_per_one * amount
    print(payed - total_price)


if __name__ == '__main__':
    main()
