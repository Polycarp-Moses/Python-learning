import random
#Generate a random integer between 1 and 100 and check if the result is an even number
random_integer = random.randint(1,100)
print(f"Random integer: {random_integer}")
is_even = (random_integer % 2) ==0
print(f"Is the number even? {is_even}")