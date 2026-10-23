#COPYING LISTS
#Methods and ways to copy data:

#Assignment = ; used to make a reference and not an extra copy. Both variables reference the same list in memory; making this a risky way of making copies
letters = ['a', 'b', 'c'] #create a copy of the list in a new variable
letters_copy = letters #assigning the original list to the new variable
letters_copy.append('z') # adding an item to the copy will also add the item to the original list
letters.pop() # removing the last item from the original list will do the sama to the copy
print('Original: ',letters)
print('copy:', letters_copy)

print()

#Shallow copy
# use the method: .copy()- creates a real extra copy not just a reference- the new copy is created by a new variable that is independent from the original list. Python stores the two lists in two independent containers. So removing or changing an item from a copy does not affect the original list

letters = ['a', 'b', 'c']
letters_copy = letters.copy()
letters_copy.append('z')
letters.append('x')
letters.pop()
print('Original: ',letters)
print('copy:', letters_copy)

print()

#Deep copy
#The copy() method creates a shallow copy as seen below
matrix = [["d", "e"],
          ['g', 'h']]
matrix_copy = matrix.copy()
matrix.pop() #remove the last row from the original matrix
matrix_copy[0].insert(0, 'k') #  add a new item in the 1st row of the copied list. This adds the new item in the copy original list too because the copy() method creates a shallow copy
print('Original matrix: ', matrix)
print('Copy matrix: ', matrix_copy)

print()
#To fix the shallow copy problem seen above, we have to import the copy module, which has two functions- copy () function and deepcopy() function. deepcopy is useful in copying everything in your matrix layer by layer to create completely independent lists in a matrix

import copy
# copy.deepcopy() creates a true, independent copy of all levels
matrix = [["d", "e"],
          ['g', 'h']]
matrix_copy = copy.deepcopy(matrix) #start with the module name (copy) then the function name (deepcopy)
matrix.pop() #now this changes the original list but does not affect the copy
matrix_copy[0].append('z') # add an item in the first row of the copy matrix
print('Original matrix: ', matrix)
print('Copy matrix: ', matrix_copy)

print()
#copy.copy() - creates a shallow copy just like the method copy () -references to the same lists within the list-does not create independent copy of a matrix
matrix = [["d", "e"],
          ['g', 'h']]
matrix_copy = copy.copy(matrix)
matrix.pop()
print('Original matrix: ', matrix)
print('Copy matrix: ', matrix_copy)