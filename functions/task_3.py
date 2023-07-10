def choose_func(numbers_list, func1, func2):
    for number in numbers_list:
        if number<0:
            return func2(numbers_list)
    return func1(numbers_list)
    

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

 

def square_nums(nums):

    return [num ** 2 for num in nums]


def remove_negatives(nums):

    return [num for num in nums if num > 0]


print(choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25])

print(choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5])