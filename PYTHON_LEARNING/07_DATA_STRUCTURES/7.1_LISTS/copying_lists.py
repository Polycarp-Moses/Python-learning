#COPYING LISTS
#Methods and ways to copy data:

#Assignment = ; used to make a reference and not an extra copy. Both variables reference the same list in memory; making this a risky way of making copies
letters = ['a', 'b', 'c'] #create a copy of the list in a new variable
letters_copy = letters #assigning the original list to the new variable
letters_copy.append('z') # adding an item to the copy will also add the item to the original list
letters.pop() # removing the last item from the original list will do the sama to the copy
print('Original: ',letters)
print('copy:', letters_copy)

#Shallow copy
# use the method: .copy()- creates a real extra copy not just a reference- the new copy is created by a new variable that is independent from the original list