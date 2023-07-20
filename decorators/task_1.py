def logger(func):
    def wrapper(*args):
        args_str=' ,'.join([str(arg) for arg in args])
        print(f"{func.__name__} called with {args_str}")

        return func(*args)
    return wrapper


@logger
def add(x,y):
    return x+y

@logger
def square_all(*args):
    return [arg**2 for arg in args]

add(2,59)
square_all(1,2,3)
