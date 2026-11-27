from car import Car #from the name of the module (car), import the name of the class(Car)

#To create a car object, you need a unique name for the car such as car1; then equal to the name of the class with a set of paranthesis to invove the constructor: i.e. car1 = Car("Audi", 2026, "red", False). Then in the brackets, you pass a matching number of arguments for the parameters. 

car1 = Car("Audi", 2026, "red", False)
car2 = Car("BMW", 2024, "Blue", True) #We can reuse the same class above to create a second car - car2 and pass some different arguments
car3 = Car("Mercedes Benz", 2025, "Black", True)

print(car1) #this prints the memory address of the car object
print(car1.model) #this prints one of the attributes - the dot(.) is known as the attribute access operator
print(car1.year)
print(car1.color)
print(car1.for_sale, "\n")

#car2
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale, "\n")

#car3
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale, "\n")

#Acess the methods
car1.drive()
car1.stop()
car2.drive()
car3.drive()
car2.stop()
car3.stop()

#Acess usingf-strings
car1.drive()
car1.stop()
car2.drive()
car2.stop()
car3.drive()
car3.stop()

#access the describe method
car1.describe()
car2.describe()
car3.describe()