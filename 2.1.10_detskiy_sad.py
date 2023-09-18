def main():
    name = input()
    cabinet = input()

    group, bed, index = list(cabinet)

    print(f"""Группа №{group}.
{index}. {name}.
Шкафчик: {cabinet}.
Кроватка: {bed}.""")


if __name__ == '__main__':
    main()
