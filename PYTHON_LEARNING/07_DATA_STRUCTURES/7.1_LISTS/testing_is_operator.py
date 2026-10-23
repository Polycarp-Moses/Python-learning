import copy
# How to check if you have two independent lists or they are sharing something
# Is operator- checks if two variables refer to the same object
#Use the is operator to check if the copies are truly independent

original = [
    ['a', 'b'],
    ['c', 'd']]

#Assignment
copy1 = original
print("Same object?", original is copy1, "\n")

#Shallow copy
copy2 = original.copy()
print("Same object?", original is copy2)
print("Shared lists?", original[0] is copy2[0], "\n")

#Deep copy
copy3 = copy.deepcopy(original)
print("Same object?", original is copy3)
print("Shared lists?", original[0] is copy3[0], "\n")
