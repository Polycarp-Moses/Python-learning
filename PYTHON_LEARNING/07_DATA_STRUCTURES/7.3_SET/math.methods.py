#SET MATH METHODS
#Methods: .union(), .intersection(), .difference(), .symmetric_difference()

#Union() -combines all unique items from both sets
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.union(b)) #start with one set then pass the other inside union method

#Note: math operators return a new set and leave the originals untouched
print(a) #this will print the same original data
print(b) #same as this

#You can use shortcut for union()
print(a | b)

#intersection() - returns only the shared items
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.intersection(b))

#shortcut for intersection()
print(a & b)

#difference () -returns items that appear in the first set but not in the second
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.difference(b)) #Returns items in A but not in B

#shortcut for difference()
print(a-b)
print(b-a) #returns items in B, but not in A

#symmetric_difference() -returns only none-shared values- unique values
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
print(a.symmetric_difference(b))

#shortcut for symmetric_difference()
print(a ^ b)