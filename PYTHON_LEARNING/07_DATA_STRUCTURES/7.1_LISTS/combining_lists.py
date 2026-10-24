# Combining
#Using the plus + operator
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers
print(comb, "\n")

#Multiplier Operator (*) - makes multiple copies of the same list
letters = ['a', 'b', 'c']
print(letters * 2, "\n")

#Splitted list/ New nested list
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = [letters, numbers]
print(comb, "\n")

# extend () method - allows you to add second list to your main list- it does't create a new list; it expands the original list
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(numbers)
print(letters, '\n') #this list will not change because we didn't modify it

#Combining using zip () - pairs items from two lists - creates a list of tuples- if one list is longer than the second one, the items without pairs will be discarded- the output will be an iterator object that will be convereted to a list using the function list()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers))
print(comb, '\n')

#zip () use case - pair customers with their IDs
ids = [101, 102, 103]
names = ['Moses', 'Morgan', 'Humphrey']
comb = list(zip(ids, names))
print(comb)