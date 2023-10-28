def main():
    objects = input().split()
    for i, obj in enumerate(objects):
        print(f'{i + 1}. {obj}')


if __name__ == '__main__':
    main()
