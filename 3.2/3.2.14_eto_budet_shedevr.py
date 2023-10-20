def main():
    products = set()
    receipts = dict()

    for _ in range(int(input())):
        products.add(input())

    for _ in range(int(input())):
        receipt_name = input()
        receipt_products = set()

        for _ in range(int(input())):
            receipt_products.add(input())
        
        receipts[receipt_name] = receipt_products
    
    found = False
    for receipt_name in sorted(receipts):
        receipt_products = receipts[receipt_name]

        if len(receipt_products - products) == 0:
            print(receipt_name)
            found = True
    
    if not found:
        print('Готовить нечего')


if __name__ == '__main__':
    main()
