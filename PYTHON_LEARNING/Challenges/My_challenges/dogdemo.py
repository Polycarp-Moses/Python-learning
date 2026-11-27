from dog import Dog

dog1 = Dog("Rex", 2, "Labrador")
dog2 = Dog("Queen", 1, "German Shepherd")

print(dog1.name)
print(dog2.breed)


#Call methods
dog1.bark()
dog2.bark()
dog1.describe()
dog2.describe()