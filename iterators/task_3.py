class CustomIterable:
    def __init__(self,data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            current_el = self.data[self.index]
            self.index+=1
            return current_el
        else:
            raise StopIteration
        
    def __getitem__(self,index):
        return self.data[index]
    

my_it = CustomIterable([1, 2, 3, 4, 70])

for i in my_it:
    print(i)

print(my_it[2])