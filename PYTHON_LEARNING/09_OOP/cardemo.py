from car import Car

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
print(car3.for_sale)