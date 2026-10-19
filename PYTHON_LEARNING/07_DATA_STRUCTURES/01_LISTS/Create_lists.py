#Create lists
#Empty list
empty = []
print(empty)
print(type(empty))

empty = list() #another way of creating an empty list
print(empty)

print()

#Create list by adding items manually
letters = ["a", "b", "c"]
print(letters)
print(type(letters))

print()

numbers = [1,2,3]
print(numbers)
print(type(numbers))

print()

#You can mix data types in the same list
mixed = [1, "a", True, None]
print(mixed)
print(type(mixed))

print()

#Create list by using built in function list()
#list(value)-built in function; converts an iterable(sequence into a list)

empty = list()
print(empty)

print()

#Create by converting - if you have the data already but in a different data type or an object, you can convert it into a list. You will get the same data but in different object
#Create a new list from already existing data using list () function
letters = list("Python")
print(letters)

print()

numbers = list(range(5))
print(numbers)