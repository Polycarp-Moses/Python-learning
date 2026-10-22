#SORTING LISTS
#Involves organizing and rearranging your data in a list

# sort()-method that sorts from smallest to biggest/ in ascending order
letters = ['c', 'a', 'b'] #sort this list in ascending order
letters.sort() #leaving the value empty means ascending order by default
print(letters)

print()
#sort from biggest to smallest/descending-use the keyword 'reverse = True'

letters = ['c', 'a', 'b']
letters.sort(reverse = True )
print(letters)

print()
#sorting a matrix -python does not check all the values of each list, instead it compares only the first values of each inner list
matrix = [["d", "e", "f"],
          ['g', 'h', 'i'],
          ["a", "b", "c"]]
matrix.sort()
print(matrix)

print()
#if two starting items in two inner lists are similar, python will check the second items of the inner lists
matrix = [["d", "e", "f"],
          ['a', 'z', 'i'],
          ["a", "a", "c"]]
matrix.sort()
print(matrix)

print()
#How do you sort specific items in a specific row?
#e.g. sort the items in the second row
matrix = [["d", "e", "f"],
          ['a', 'z', 'i'],
          ["a", "b", "c"]]
matrix[1].sort()
print(matrix)

print()
#What if you want to leave the original list as it is and you want to create a new list where the items are sorted? You use the sorted() function
letters = ['c', 'a', 'b']
new_list = sorted(letters)
print('original list:', letters)
print('sorted list:', new_list)

print()
#what if you want to sort in descending order? (from highest to the lowest)
letters = ['c', 'a', 'b']
new_list = sorted(letters, reverse=True)
print('original list:', letters)
print('sorted list:', new_list)
