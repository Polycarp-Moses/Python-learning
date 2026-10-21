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

#REMOVE ITEMS