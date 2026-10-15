#Print a left-aligned pyramid of stars with 6 rows using a for loop

for row in range(1,7):
    print("*" * row)

print()
#Print numbers 1 to 5, each with its square

for number in range (1,6):
    new_number = number * number
    print(f"{number} squared is {new_number}")