#create class of car
# To construct a car object, we need a special type of method called a constructor. It works similarly to a function. e.g. def__init__(self). It is a dunder method, meaning double underscore. init here means initialize. Then you pass some attributes. Self is already provided. Self means this object we are creating right now i.e this car in the example below. Then you pass other parameters such as model, year, color, for_sale. To assign these attributes (model, year, color, for_sale), you access self; eg, self.model = model(when we receive the name of the model, we will assign it here). To create a car object, you need a unique name for the car such as car1; then equal to the name of the class with a set of paranthesis to invove the constructor: i.e. car1 = Car("Audi", 2026, "red", False). Then in the brackets, you pass a matching number of arguments for the parameters. 

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale