from sys import stdin


def main():
    text_nums = []
    for line in stdin:
        text_nums += line.rstrip('\n').split()
    
    print(sum([int(i) for i in text_nums]))


if __name__ == '__main__':
    main()
