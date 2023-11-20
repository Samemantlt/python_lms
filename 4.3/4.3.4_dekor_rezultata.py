def answer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'Результат функции: {result}'
    
    return wrapper
