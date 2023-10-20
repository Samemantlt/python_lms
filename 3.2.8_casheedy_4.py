def main():
    food_map = dict()
    
    for _ in range(int(input())):
        words = input().split(' ')
        
        name = words[0]
        food_types = words[1:]

        for food_type in food_types:
            if food_type not in food_map:
                food_map[food_type] = set()
            
            food_map[food_type].add(name)
    
    selected_type = input()

    if selected_type not in food_map:
        print('Таких нет')
        return
        
    for name in sorted(food_map[selected_type]):
        print(name)


if __name__ == '__main__':
    main()
