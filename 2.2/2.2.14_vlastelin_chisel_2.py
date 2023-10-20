def get_min(text: str):
    zeros = text.count('0')
    sorted_text = sorted(filter(lambda a: a != '0', list(text)))

    if zeros == 0:
        return f'{sorted_text[0]}{sorted_text[1]}'

    if zeros == 1:
        return f'{sorted_text[0]}0'

    if zeros == 2:
        return '0'


def main():
    num = input()
    sorted_text = sorted(list(num), reverse=True)
    max_num = f'{sorted_text[0]}{sorted_text[1]}'
    min_num = get_min(num)

    print(f'{min_num} {max_num}')


if __name__ == '__main__':
    main()
