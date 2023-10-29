from sys import stdin


def avg(seq):
    return sum(seq) / len(seq)


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    
    print(round(avg([int(i.split()[2]) - int(i.split()[1]) for i in lines])))


if __name__ == '__main__':
    main()
