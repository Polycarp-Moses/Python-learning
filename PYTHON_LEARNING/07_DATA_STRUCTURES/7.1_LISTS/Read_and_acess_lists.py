#Read and Acess Lists

#Reading all items inside a list
lst = ["a", "b", "c", "d"]
print(lst)

#What if you want to access only one item?
#You use INDEXING
#The index number helps you access the item you want in a list
#Positive index-start counting from zero going forward
#Use negative index to access items from the end of a list

lst = ["a", "b", "c", "d"]
print(lst[0]) #gives the first item
print(lst[3]) #gives the last item
print(lst[1])
print(lst[2])
print(lst[-1]) #using negative index to get the last item

#Access and Read Nested List (Matrix)
#You need the specific numbers for the row and column
# You have to be spefic on what you are trying to access: either the whole list, an entire row, or a specific value from a row
#Columns: 0  1  2
#Row 0   [a, b, c]
#Row 1   [d, e, f]
#Row 2   [g, h, 1]

matrix = [["a", "b", "c"], #Row 0
          ["d", "e", "f"], #Row 1
          ["g", "h", "i"]] #Row 2

#Get the whole matrix
print(matrix)

#Get the last row of the matrix
print(matrix[2]) 
print(matrix[-1]) #negative index- good practice to use because you will always mostly have multiple 

#Get the last item of the last row
print(matrix[-1][-1])

#Get the first item of the first row
print(matrix[0][0])

#Get the value in the middle
print(matrix [1][1])

#SLICING
#Retrieve multiple items in a list

lst = ["a", "b", "c", "d"]

#Get the first two items from the list
print(lst[:2])

#Get the last two items from the list
print(lst[2:])

#Get the whole list
print(lst[:])

#We can also slice a 

#Get the first two rows (lists) from a list

matrix = [["a", "b", "c"], #Row 0
          ["d", "e", "f"], #Row 1
          ["g", "h", "i"]] #Row 2
print(matrix[:2]) #We excluded the first index zero because it is default. Then we use 2 as the last index but 2 is not included

print()

#Get the last tow rows (lists) from a list
print(matrix[1:])

print()

#Get specific items from a specific row; for example get "g" and "h" from row 2
print(matrix[2][0:2]) #You can leave out the zero because it is the default starting index
