# ITERATORS AND ITERABLESS - How to iterate
# How and why we iterate?
letters = ['a', 'b', 'c']
for letter in letters:
    print(letter, '\n') #python will iterate through all items in the list above and print it. This is possible because the list is iterable.

# we use iteration to transfrom data
letters = ['a', 'b', 'c']
for letter in letters:
    print(letter.upper(), '\n') #Data transformed here into uppercase

#Store the transformed results in a new list- here we iterate through the original list, do some transformations, then store the new values in a new list
letters = ['a', 'b', 'c']
new_list = []
for letter in letters:
    new_list.append(letter.upper())
    print(new_list, '\n')

# ITERATORS: enumerate, reversed, zip
#enumerate (iterable) -Built in function- it takes any iterable like a list or string value and gives back both the index and the value
letters = ['a', 'b', 'c']
print(enumerate(letters)) #this will return a iterator. so you will need to convert it to a list
print(list(enumerate(letters)))
print(list(enumerate(letters, start = 1,))) #You can define the index number from which you want to start

print()

#Use iterator to build for loop
#enumerate is an iterator that we can use in a for loop to iterate through values
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters): 
    print(index, letter, '\n')

#Enumaerate use case: find the exact position of the bad data in your list. e.g find position of an empty value in a string
letters = ['a', '', 'c']
for index, letter in enumerate(letters): 
    print(index, letter, '\n')

#Reversed - returns an iterator that flips the data order
letters = ['a', 'b', 'c']
print(list(reversed(letters)))

print()

#Use it in for loop
letters = ['a', 'b', 'c']
for letter in reversed(letters): #returns an iteration that starts from the end to the start
    print(letter, '\n')

#using zip() function to create iterators- zip combines two or more sequences into pairs (tuples)
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for letter, number in zip(letters, numbers): #iterate between two lists using the zip function
    print(letter, number, '\n')

#Map(function, iterable)- helps you do data transformation- you give it the function that you want to repeat for each item and the iteratable. Output will be a map iterator object, so you will need to change the data type
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters))) #str.upper means used the upper method found in the string class

#task: convert list items to integers
numbers = ['1', '2', '3']
print(list(map(int, numbers)))

#task: clean up the list by removing all unwanted spaces
names = [' Maria ', 'John ', ' Kumar']
print(list(map(str.strip, names)))

print()

#task: use map function in the for loop to iterate through the values and not print it as a list
names = [' Maria ', 'John ', ' Kumar']
for name in map(str.strip, names):
    print(name, '\n')

#filter(function, iterable)-helps filter out any bad data that you don't want in your list. Output is also filter iterator object that you will need to transform
#task: clean up list by removing unvalid data
letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters))) #None removes all falsy values like 0, '', or False on top of None
print(list(filter(bool, letters))) #bool also works the same- it filters out all falsy values

#task: keep only letters(alphabetic) items
items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))

#use a for loop to iterate through the output of the filter function
items = ['sql', '123', 'python', '42']
for item in filter(str.isalpha, items):
    print(item)