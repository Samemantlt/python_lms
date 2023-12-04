import re


PACKET_RE = re.compile(r'^(?P<text>.+)\^(?P<start>\d+)\^(?P<end>\d+)$')


def parse_packet(packet: str) -> (str | int | int):
    match = PACKET_RE.fullmatch(packet)

    text = match.group('text')
    start = match.group('start')
    end = match.group('end')

    return text, int(start), int(end)


def main():
    count = int(input())
    
    for i in range(count):
        line = input()
        text, start, end = parse_packet(line)
        length = len(text)
        for i in range(start, min(end, length), length % 4):
            print(text[i], end='')
        print()


if __name__ == '__main__':
    main()
