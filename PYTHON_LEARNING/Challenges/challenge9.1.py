# Print the 7-times table from 1 to 10 using a for loop
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    result = 7 * number
    print(f"7 * {number} = {result}")

print()

#using range()
for number in range (1,11):
    print(f"7 * {number} = {7 * number}")