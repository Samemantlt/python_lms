from sys import stdin
import json


def main():
    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))

    with open('scoring.json') as file:
        groups = json.load(file)
    
    input_iter = iter(lines)

    score = 0

    for group in groups:
        all_points = group['points']
        
        tests = group['tests']
        points_per_test = all_points // len(tests)

        for test in tests:
            pattern = test['pattern']
            inp = next(input_iter)
            if inp == pattern:
                score += points_per_test
    
    print(score)


if __name__ == '__main__':
    main()
