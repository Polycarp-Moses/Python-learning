import random
random_integer = random.randint(1,100)
print(f"Generated random integer: {random_integer}")
raised_number = random_integer ** 3
print(f"Raised number: {raised_number}")
divided_number = raised_number // 4
print(f"Final calculated number: {divided_number}")
print(type(divided_number))