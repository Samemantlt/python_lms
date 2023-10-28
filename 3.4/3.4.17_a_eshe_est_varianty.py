import itertools


def main():
    obligatory_category = input()
    disallowed_value = input()
    target = input()

    match obligatory_category:
        case 'пики':
            obligatory_category = 'пик'
        case 'буби':
            obligatory_category = 'бубен'
        case 'трефы':
            obligatory_category = 'треф'
        case 'черви':
            obligatory_category = 'червей'

    values = sorted([
        *[str(i) for i in range(2, 10 + 1)],
        'валет',
        'дама',
        'король',
        'туз',
    ])

    categories = sorted([
        'пик',
        'треф',
        'бубен',
        'червей'
    ])
    
    all_combinations = itertools.product(values, categories)

    last_done = False

    for cards in itertools.combinations(all_combinations, 3):
        if any(map(lambda a: a[0] == disallowed_value, cards)):
            continue

        if not any(map(lambda a: a[1] == obligatory_category, cards)):
            continue

        current = ', '.join([f'{value} {category}' for value, category in cards])
        if last_done:
            print(current)
            return
        
        if current == target:
            last_done = True


if __name__ == '__main__':
    main()
