#Else in loop
#Runs a block of code only if the loop finishes naturally
#Loop completed without breaks


items = [1,2,3,4,7]
for i in items:
    print(i)
else:
    print("Loop is complete")

print()

#Else + Break
#Use else with loops only when there is a break
#else will run only if the loop is not interrupted
#Task: Find out if there are even numbers
items = [1,2,3,4,7]
for i in items:
    if i % 2 == 0:
        print("Even number found:", i)
        break
else:
    print("All numbers are odd") #else will run only if the loop is not interrupted