#Sum to N: Ask the user for a Number N, then print the sum of 1 + 2 + ... + N.

n = int(input("Enter a number: "))

total = 0
number = 1

while number <= n:
    total = total + number
    number = number + 1
print(total)
