in_stock = {"coffee": 1, "milk": 2, "cream": 3}

coffee_recipes = {
    'Эспрессо': {
        'coffee': 1
    },
    'Капучино': {
        'coffee': 1,
        'milk': 3
    },
    'Макиато': {
        'coffee': 2,
        'milk': 1
    },
    'Кофе по-венски': {
        'coffee': 1,
        'cream': 2
    },
    'Латте Макиато': {
        'coffee': 1,
        'milk': 2,
        'cream': 1
    },
    'Кон Панна': {
        'coffee': 1,
        'cream': 1
    }
}


def can_cook(recipe_name: str):
    ingredients = coffee_recipes[recipe_name]

    for key, value in ingredients.items():
        if in_stock[key] < value:
            return False
    
    return True


def cook(recipe_name: str):
    ingredients = coffee_recipes[recipe_name]

    for key, value in ingredients.items():
        in_stock[key] -= value


def order(*prefers):
    for recipe in prefers:
        if can_cook(recipe):
            cook(recipe)
            return recipe
    
    return "К сожалению, не можем предложить Вам напиток"


if __name__ == '__main__':
    main()
