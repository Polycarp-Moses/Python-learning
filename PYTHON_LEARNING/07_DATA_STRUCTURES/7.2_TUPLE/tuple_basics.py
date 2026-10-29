#TUPLE - an ordered collection that can't be changed after creating it.
# You mostly use tuples when you feel your data is protected and shouldn't be changed
#syntax and characteristics:

# 1. Tuple is ordered - python will keep the order as you defined it
my_tuple = (10, 30, 20)
print(my_tuple) #ordered

# 2. Tuple allows duplicates
my_tuple = (10, 30, 20, 10)
print(my_tuple)

#3. Tuple is indexed - you can access any value using indexing
my_tuple = (10, 30, 20, 10)
print(my_tuple[1])

# 4. Tuple is immutable -items in a tuple can't be changed
my_tuple = (10, 30, 20, 10)
my_tuple[2] = 40