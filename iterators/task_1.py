def with_index(iterable, start = 0):
    index = start
    for i in iterable:
        yield i, index
        index+=1

list_1 = [1, 2, 3, 70]
for value, index in with_index(list_1):
    print(f"Value : {value}, index : {index} ")