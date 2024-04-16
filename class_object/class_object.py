class Person:
    def __init__(self,name,age,gender,disability):
        self.name = name
        self.age = age
        self.gender = gender
        self.disability = disability

    def speak(self):
        return f"{self.name} says Hello"
    def say_age(self):
        print(f"{self.name} is {self.age}years old")
    def say_disability(self):
        print(f"{self.name} has {self.disability}")
    def say_gender(self):
        print(f"{self.name} is {self.gender}")


divya = Person("Divya","18","female","no disability")
print(divya.speak())
divya.say_age()
divya.say_disability()
divya.say_gender()


class Animal:
    def __init__(self):
        self.name = name
        self.species = species
        self.age = age

def walk(self):
    print(f"{self.name} is walking")

def eating(self):
    print(f"{self.name} is eating")

class Cat(Animal):
    def __init__(self,name,species,age):
        super().init_(name,species,age)
        self.color = color
kitty = Cat("kitty","british shorthair", 3)
print(kitty.speak())
kitty.species()
kitty.age()

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Fish:
    def __init__(self,name,sea,age):
        self.name = name
        self.sea = sea
        self.age = age
    def swim(self):
        print(f"{self.name} can swim")
    def breathe(self):
        print(f"{self.name} can breathe")

class Shark(Fish):
    def bite(self):
        print(f"{self.name} may bite")

jaws = Shark("jaws","pacific","12")
jaws.bite()