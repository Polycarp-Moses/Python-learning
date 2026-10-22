#CHANGING YOUR LISTS
# ADD ITEMS

# Easiest way is just appending/adding the new value at the end of the list. To do this use the method . append(value)
letters = ['a', 'b', 'c']
letters.append('x') #Add 'x' to the end of the list
letters.append('y') #Add 'y' to the end of the list
print(letters)

print()

#What if you want to insert a value at a specific position? Use the .insert method(index, value)
letters = ['a', 'b', 'c']
letters.insert(0, 'f') #insert 'f' at the start of the list
letters.insert(3, 'y') #add 'y' between 'b' and 'c'. Here we are using the new output from above to get the index
print(letters)

#Add a new row to the end of matrix
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix.append(['x', 'y', 'z'])
print(matrix)

print()

#Add a new row at the start of Matrix. Here you use insert method
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix.insert(0, ['t', 'p', 'k'])
print(matrix)

# Add 'x' at the end of the second row
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[1].append('x')
print(matrix)

print()

#Add 'z' at the start of the first row
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[0].insert(0, 'z')
print(matrix)

print()

#REMOVE ITEMS
#clean up your list by removing duplicate data, old data or bad data that could corrupt your list
#Remove everything
letters = ['a', 'b', 'c']
letters.clear()
print(letters)

print()

#Remove a specific value
#- remove by value
letters = ['a', 'b', 'c']
letters.remove('a')  #remove 'a from the list
print(letters)

print()

#-remove by position
letters = ['a', 'b', 'c']
removed = letters.pop() #removes last item by default if you dont's specify the index. variable created here to store the removed item; otherwise, letters.pop() to output the new list after item is removed
print(letters)
print('Removed item:', removed)

print()
#remove the first item
letters = ['a', 'b', 'c']
removed = letters.pop(0)
print(letters)
print('Remobved item:', removed)

print()
#remove the middle item
letters = ['a', 'b', 'c']
removed = letters.pop(1)
print(letters)
print('Removed item:', removed)

print()
#Remove list from a matrix
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix.remove(['a', 'b', 'c']) #remove by value
print(matrix)

print()

#remove the last row
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix.pop() #remove by position-default removes last row; index not specified
print(matrix)

print()

#Remove a specific value; e.g remove 'e' from the matrix
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[1].remove('e') #first specify the row, then the value
print(matrix)

print()

#Remove the first item from the last row
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[-1].pop(0) #Remove by position
print(matrix)

print()

#Remove the last item of the first list
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[0].pop()
print(matrix)

print()

#UPDATE ITEMS
#update the first item to the value 'x
letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y' #update the second item
print(letters)

print()

#update Matrix
#update content of the last list
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[-1] = ['m', 'n', 'o']
print(matrix)

print()
#update the first item of the first row
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[0][0] = '-'
print(matrix)

#update the middle item 'e'
matrix = [["a", "b", "c"], 
          ["d", "e", "f"],
          ['g', 'h', 'i']]
matrix[1][1] = '-' #update the middle item 'e'
matrix[-1][-1] = '-' #update last item of the last row
print(matrix)