#SETS - unordered collection of unique values
#Syntax and characteristics:
# 1. Set is unordered - python changes the order that you define. Unlike in lists where items are stored in an array, where each item seats next to each other in memory and has their index number; in sets items are stored differently, where a hash function 'f(x)' generates critical values, and each item is stored based on the critical values randomly and not by the index numbers. The advantage for sets in python is speed in checking whether a value exists.

my_sets = {10, 30, 20}
print(my_sets)

# 2. Set is unique (does not allow duplicates) - very useful in storing unique sets of data like customer ids.
my_sets = {10, 30, 20, 10}
print(my_sets)

# 3. Set is NOT indexed
my_sets = {10, 30, 20, 10}
#print(my_sets[1])

# 3. Set is mutable
my_sets = {10, 30, 20}
my_sets.remove(20)
print(my_sets)