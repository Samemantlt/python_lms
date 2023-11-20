def result_accumulator(func):
    queue = []

    def wrapper(*args, **kwargs):
        nonlocal queue
        
        method_drop = kwargs.get('method') == 'drop'
        
        if 'method' in kwargs:
        	del kwargs['method']

        result = func(*args, **kwargs)

        if method_drop:
            last = queue
            queue = []
            return last
        else:
            queue.append(result)
            return None
    
    return wrapper
