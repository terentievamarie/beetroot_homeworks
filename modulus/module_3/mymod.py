def count_lines(name):
    with open(name,'r') as file:
        return len(file.readlines()) # returns a list with strings
    
def count_chars(name):
    with open(name,'r') as file:
        return len(file.read())
    
def test(name):
    with open(name,'r') as file:
        quantity_of_lines=count_lines(name)
        file.seek(0)
        quantity_of_chars=count_chars(name)
        print(quantity_of_lines)
        print(quantity_of_chars)


