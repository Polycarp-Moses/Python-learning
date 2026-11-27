# oop challenges

# Create dog.py with a Dog class that has name, age and breed

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Add a method bark() that prints "Rex says woof!", using the dog's name

    def bark(self):
        print(f"{self.name} says woof!")

    #Add a method describe() that prints something lime "Rex is 3 years old and is a Labrador"

    def describe(self):
        print(f"{self.name} is {self.age} years old and is a {self.breed}")

