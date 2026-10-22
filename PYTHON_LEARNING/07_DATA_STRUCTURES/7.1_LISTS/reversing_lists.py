# REVERSING LISTS
#Say you don't care about the order of data
#You just want to flip the list around
#We use the reverse() method -this is different from the argument reverse=True that we used in sorting lists
#reverse() is a dedicated method that flips the list so that the last value becomes the first and the first the last

letters = ['c', 'a', 'b']
letters.reverse()
print(letters)

print()
#We can print a new list and leave the original list as was using the reversed () function. But note that the reversed () function here creates an iterator object, not a list object. So you convert the data type from iterator to list by using the list() function
letters = ['c', 'a', 'b']
new_list = list(reversed(letters))
print('original list:', letters)
print('reversed list:', new_list)




