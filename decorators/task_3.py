def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(argument):
            
            if not isinstance(argument, type_):
                print(f"Invalid argument type. Expected: {type_.__name__}")
                return False

            
            if len(argument) > max_length:
                print(f"Argument length is too much ")
                return False

            
            if contains:
                if not any(symbol in argument for symbol in contains):
                    print(f"Argument must contain at least one of the specified symbols: {contains}")
                    return False

            
            return func(argument)

        return wrapper

    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com') )
print(create_slogan('S@SH05')) 