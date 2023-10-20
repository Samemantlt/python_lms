def main():
    count = int(input())
    
    for i in range(count):
        times = 3 + i
        for j in range(times, 0, -1):
            print(f'До старта {j} секунд(ы)')
        print(f'Старт {i + 1}!!!')


if __name__ == '__main__':
    main()
