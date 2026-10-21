#Explore and Analyze Lists
#Functions:

#Max() - Function that finds the highest value in a list. Outputs the value
numbers = [1,5,2,4,3]
print("Max:", max(numbers))

#Min() - Function that finds the lowest value in a list
numbers = [1,5,2,4,3]
print("Minimum:", min(numbers))

#Sum() -Function that finds the total by summing all values. Outputs the number. Does not work if there are string values in a list; only numbers
numbers = [1,5,2,4,3]
print("Total:", sum(numbers))

#len () -Function that finds the length of a list (number of items). Outputs number. This functions works for any data type including string and boolean
numbers = [1,5,2,4,3]
print("Length:", len(numbers))

#all() - Checks if all items are true. Returns True if all values are True
numbers = [1,5,2,4,3]
print("All:", all(numbers)) #Returns True because we have real values for each item
numbers = [1,0,2]
print("All:", all(numbers)) #Returns False because zero is considered a missing value
print("All:", all(['a', '', 'c'])) #Same for string. Returns False because there is a missing value
print("All:", all(['a', 'b', 'c']))

#Any()- Did something pass? Returns True if you have at least one True value
numbers = [1,5,2,4,3]
print("Any:", any(numbers))
print("Any:", any(['a', '', 'c']))
print("Any:", any(['a', 'b', 'c']))
print("All:", all([0, 0, 0]))
print("Any:", any(['', '', '']))

#METHODS
#.count(value)- method that returns how many times a value appears on a list. Helps you check if your values are unique or you have duplicated your list
numbers = [1,5,2,4,3, 5]
print("Count:", numbers.count(5))

#.index(value)- Method that returns the position of the first occurrence of a value
numbers = [1,5,2,4,3, 5]
print("Index:", numbers.index(5)) #returns position of the first appearance of 5

#OPERATORS
#in operator- checks if a value exists in a sequence
numbers = [1,5,2,4,3, 5]
print(4 in numbers)
print(8 in numbers)
print(8 not in numbers) #combines not + in

# == comparison operator
list1 = [1,2,4]
list2 = [1,2,4]
print(list1 == list2)

# < less than comparison operator; The first elements are compared, if they are equal, Python moves to the next element
list1 = [1,2,4]
list2 = [5,2,4]
print(list1 < list2)

#is operator -checks whether values have the same memory address
list1 = [1,2,4]
list2 = [1,2,4]
print(list1 is list2)