def oops():
    raise IndexError("Oops! IndexError occurred.")


def print_element(list_1):
    try:
        print(list_1[4])
    except IndexError:
        oops()

print(print_element([4,3,5,3]))
 #or

def calculate(my_list):
    try:
        print(my_list[0]+my_list[300])
    except IndexError:
        oops()

print(calculate([11,12,55,44,53]))


