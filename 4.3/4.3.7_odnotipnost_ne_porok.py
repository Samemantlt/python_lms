def same_type(func):
    def wrapper(*args):
        t = type(args[0])
        for arg in args:
            if not isinstance(arg, t):
                print('Обнаружены различные типы данных')
                return None

        return func(*args)
    
    return wrapper
