# In for loop, we must always spefify the sequence. 
#Sequences can be inform of a tuple, list, string, range, etc.

#list sequence:
items = [1,2,3,4,"Hi"] #square brackets means a list
for item in items:
    print(f"Item: {item}")

print()

#string:
#A string is a sequence of letters
items = "Python"
for item in items:
    print(f"Round: {item}")

print()

#range:
#It is a build in function
#range(stop): the stop argument-if start is not defined, it will always start at zero
for item in range(5):
    print(f"Round: {item}")

print()

#range(start,stop): you can add the start and stop arguments
for item in range(1,6):
    print(f"Round: {item}")

print()
#range(start, stop, step): the step argument is added to define the incrementation. If you don't define it, the default incrementation is always 1.

for item in range(0,10,2):  #generate all even numbers between 0 and 10
    print(f"Round: {item}")

print()

for item in range(1,10, 2):  #generate all odd numbers between 0 and 10
    print(f"Round: {item}")