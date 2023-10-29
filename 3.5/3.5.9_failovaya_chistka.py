def main():
    filename = input()
    with open(filename) as file:
        text = file.read()

    filename = input()

    lines = text.splitlines()

    formatted_lines = []
    for i in lines:
        if i.isspace() or i == '':
            continue
        formatted_lines.append(' '.join([j for j in i.replace('\t', '').split(' ') if j != '']))

    with open(filename, 'w') as file:
        for line in formatted_lines:
            file.write(line + '\n')


if __name__ == '__main__':
    main()
