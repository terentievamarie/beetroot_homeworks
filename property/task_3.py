from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)
        return wrapper


@TypeDecorators.to_bool
def do_bool(string: str):
    return string


@TypeDecorators.to_int
def do_int(string: str):
    return string


@TypeDecorators.to_str
def do_str(num: int):
    return num


print(do_bool("True") == True)
print(do_int("13") == 13)
print(do_str(1999) == '1999')