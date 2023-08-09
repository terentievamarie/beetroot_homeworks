class Animal:

    def talk(self):
        print("I like talking")

class Dog(Animal):

    def talk(self):
        print("Woof woof!!")

class Cat(Animal):
    
    def talk(self):
        print("Meow meow")


def animal_talk(instance):
    instance.talk()

animal_1=Animal()
animal_talk(animal_1)

dog_1=Dog()
animal_talk(dog_1)

cat_1=Cat()
animal_talk(cat_1)   