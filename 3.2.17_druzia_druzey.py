def main():
    lines = []

    while (line := input()) != '':
        lines.append(line)
    
    firends_dict = dict()

    def add_friends(a: str, b: str):
        if a not in firends_dict:
            firends_dict[a] = set()
        if b not in firends_dict:
            firends_dict[b] = set()

        firends_dict[a].add(b)
        firends_dict[b].add(a)

    for line in lines:
        a, b = line.split(' ')
        add_friends(a, b)
    
    def get_ith_friends(user, index):
        if index == 0:
            return firends_dict[user]
        else:
            res = set()

            for local_friend in firends_dict[user]:
                next_firends = get_ith_friends(local_friend, index - 1)
                res = res.union(next_firends)
            
            return res

    for name in sorted(firends_dict):
        friends = get_ith_friends(name, 1) - get_ith_friends(name, 0)
        res = friends - {name}
        print(f'{name}: {", ".join(sorted(res))}')


if __name__ == '__main__':
    main()
