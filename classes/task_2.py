# Create a class Dog with class attribute 'age_factor' equals to 7.
#  Make __init__() which takes values for a dog’s age.
#   Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor=7

    def __init__(self,dogs_age):
        self.dogs_age=dogs_age

    def human_age(self):
        return self.dogs_age*self.age_factor
    
husky=Dog(2)
print(husky.human_age())

