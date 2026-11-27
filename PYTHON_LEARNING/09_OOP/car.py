#create a class of car
# To construct a car object, we need a special type of method called a constructor. It works similarly to a function. e.g. def__init__(self). It is a dunder method, meaning double underscore. init here means initialize. Then you pass some parameters. Self is already provided. Self means this object we are creating right now i.e this car in the example below. Then you pass other parameters such as model, year, color, for_sale. To assign these attributes (model, year, color, for_sale), you access self; eg, self.model = model(when we receive the name of the model, we will assign it here). For better organization, we have created another python file (cardemo.py) to access/print the attributes and methods.

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    #define a method within a class (methods are functions that belong to an object - they are actions that our objects can perform)

    def drive(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

    #You can convert the print statements to f-strings
    def drive(self):
        print(f"You drive the {self.color} {self.model}") #self here refers to the object we are currently working with, followed by the attribute access operator (.), followed by the name of the attribute(model)
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")