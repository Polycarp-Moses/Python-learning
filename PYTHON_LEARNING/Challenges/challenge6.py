import random
#Generate a random integer between 1 and 100 and check if the result is an even number
x= random.randint(1,100)
print(f"Generated number: {x}")
is_even = (x % 2) == 0
print(f"Is the number even?: {is_even}")