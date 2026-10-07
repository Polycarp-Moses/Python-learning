import random
#Generate a random integer between 1 and 100 and check if the result is an even number
random_int = random.randint(1,100)
print(f"Generated integer: {random_int}")
is_even = (random_int % 2) == 0
print(f"Is the result an even number? {is_even}")