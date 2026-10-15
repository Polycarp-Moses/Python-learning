import random
import math
random_integer = random.randint(10,50)
print(f"Generated random integer: {random_integer}")
square_root = math.sqrt(random_integer)
print(f"Square root: {square_root}")
whole_number = math.floor(square_root)
print(f"Whole number: {whole_number}")
print(type(whole_number))