def print_sum_of_arguments():
    def sum_of_aquared_arguments(a,b):
        result=a**2 + b**2
        return result
    
    return sum_of_aquared_arguments

print(print_sum_of_arguments()(3,5))
