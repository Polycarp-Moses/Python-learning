#SET RELATIONSHIP METHODS
#Used to check the relationship between two sets

#issubset() - returns True if ALL items in the set exist in the order
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = {30, 40}
print(a.issubset(b))
print(c.issubset(b)) # C is a subset of b

#issuperset() - returns True when it includes ALL items of the other set
a = {30, 40}
b = {30, 40, 50, 60}
print(b.issuperset(a)) # b includes all items of a

#isdisjoint() - returns true if both sets share no items (No Overlapping)
a = {30, 40}
b = {30, 40, 50, 60}
c = {70, 90}
print(a.isdisjoint(b))
print(b.isdisjoint(c))

#usecases:
#You can use issubset() and issuperset() when you have two tables and you want to check whether values in one table appear in the other
#isdisjoint() is used when you want to split a table into two and check whether there are overlapping values