def count_local_variables(*args):
    local_1 = 1
    local_2 = 3
    local_3 = 7
    return len(locals())

print(count_local_variables(1, 2, 3, 4))

# or
def count_local_variables_2(number_1,number_2,number_3):
    local_1 = 1
    local_2 = 3
    local_3 = 7
    return len(locals())

print(count_local_variables_2(1,2,3))
