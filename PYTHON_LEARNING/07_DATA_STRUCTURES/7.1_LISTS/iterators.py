# # ITERATORS AND ITERABLES - An iterator is something that hands you items one at a time and remembers where it is. It is an object that does the looping; it hands you the next item and remembers where it stopped. On the other hand, Iterable is something you can go through: a list, string, tuple, dictionary; while iterator is the thing that does the going through and keeps track of the position.
# # #Why iterators matter? They are lazy: i.e. they produce items only when asked, instead of building a whole new list in memory. That matters with large data, like reading a file with a million rows.
# #Examples of iteration: (iteration means going through items one at a time).

letters = ['a', 'b', 'c'] #How does python know how to go through this list? The answer is that the list is iterable or a list you can loop over. So a for loop can go through it. Python creates an iterator behind the scenes to do that.
for letter in letters: #A for loop is a way of asking for the next item until there are none left -a for loop is the act of iterating
     print(letter, '\n') #python will iterate through all items in the list above and print it. This is possible because the list is iterable.

# # we use iteration to transform data
letters = ['a', 'b', 'c']
for letter in letters:
    print(letter.upper(), '\n') #Data transformed here into uppercase

# #Store the transformed results in a new list- here we iterate through the original list, do some transformations, then store the new values in a new list. 
letters = ['a', 'b', 'c'] #the original list
new_list = [] #an empty list, to collect results
for letter in letters:
    new_list.append(letter.upper()) #letter.upper()-makes it capital; new_list.append()-adds the capital to the end of the new list
    print(new_list, '\n')

# # # ITERATORS: enumerate, reversed, zip, map, filter. 
# # #These are built in iterators- they are iterators we can actually hold and use ourselves
# # #enumerate (iterable) -Built in function- it takes any iterable like a list or string value and gives back both the index and the value
letters = ['a', 'b', 'c']
print(enumerate(letters)) #this will return a iterator. so you will need to convert it to a list
print(list(enumerate(letters)))
print(list(enumerate(letters, start = 1,))) #You can define the index number from which you want to start

print()

# #Use iterator to build for loop
# #enumerate is an iterator that we can use in a for loop to iterate through values
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters): 
    print(index, letter, '\n')

# # #Enumerate use case: find the exact position of the bad data in your list. e.g find position of an empty value in a string
letters = ['a', '', 'c']
for index, letter in enumerate(letters): 
    print(index, letter, '\n')

# #Reversed - returns an iterator that flips the data order - goes from end to start
letters = ['a', 'b', 'c']
print(list(reversed(letters)))

print()

# # #Use it in for loop
letters = ['a', 'b', 'c']
for letter in reversed(letters): #returns an iteration that starts from the end to the start
    print(letter, '\n')

# #using zip() function to create iterators- zip combines two or more sequences into pairs (tuples) - that is, it pairs up two lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for letter, number in zip(letters, numbers): #iterate between two lists using the zip function
    print(letter, number, '\n')

# #Map(function, iterable)- an iterator that applies a function to every item- helps you do data transformation- you give it the function that you want to repeat for each item and the iteratable. Output will be a map iterator object, so you will need to change the data type
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters))) #str.upper means use the upper method found in the string class

# # #task: convert list items to integers
numbers = ['1', '2', '3']
print(list(map(int, numbers)))

# #task: clean up the list by removing all unwanted spaces
names = [' Maria ', 'John ', ' Kumar']
print(list(map(str.strip, names)))

print()

# # #task: use map function in the for loop to iterate through the values and not print it as a list
names = [' Maria ', 'John ', ' Kumar']
for name in map(str.strip, names):
    print(name, '\n')

# #filter(function, iterable)-helps filter out any bad data that you don't want in your list. Output is also filter iterator object that you will need to transform
# #task: clean up list by removing unvalid data
letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters))) #None removes all falsy values like 0, '', or False on top of None
print(list(filter(bool, letters))) #bool also works the same- it filters out all falsy values

# # #task: keep only letters(alphabetic) items
items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))

# #use a for loop to iterate through the output of the filter function
items = ['sql', '123', 'python', '42']
for item in filter(str.isalpha, items):
    print(item)