def main():
    s = 0
    while (price := float(input())) != 0:
        if price >= 500:
            s += price * 0.9
        else:
            s += price
    print(s)


if __name__ == '__main__':
    main()
