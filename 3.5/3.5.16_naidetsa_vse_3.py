from sys import stdin


def match_query(text: str, query: str) -> bool:
    normalized_text = ' '.join([i.lower() for i in text.split() if not i.isspace() and i != ''])

    return query.lower() in normalized_text


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    
    query = lines[0]
    filenames = lines[1:]

    result = []

    for filename in filenames:
        with open(filename) as file:
            text = file.read()
        if match_query(text, query):
            result.append(filename)
    
    if len(result) == 0:
        print('404. Not Found')
    else:
        for filename in result:
            print(filename)


if __name__ == '__main__':
    main()
