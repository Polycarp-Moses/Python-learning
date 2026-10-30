# SET METHODS

#HOW TO ADD VALUES TO SET
# - index-based methods do not work with sets
# - instead, use the method add() - which inserts the item somewhere in the set, but only if it is new

a = {10, 20, 30, 40}
a.add(50)
print(a)

# How about adding multiple values in a set?
# Use the method update() - which merges another group of values (Iterable) into the set

a = {10, 20, 30, 40}
a.update('hi') #string
a.update([7, 9]) #list
a.update({4, 6}) #set
print(a)

#Note: we can use math operators as quick shortcuts: |&-
# |= works like update for sets
a = {10, 20, 30, 40}
a |= {1,3}
print(a)

#HOW TO REMOVE VALUES FROM SET
# discard() method removes the item if it exists and does nothing if it does not
a = {10, 20, 30, 40}
a.discard(10)
print(a)