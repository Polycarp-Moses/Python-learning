import random
float_number = random.random()
print(f"Generated random floating number: {float_number}")
scaled_number = float_number * 50
print(f"Scaled number is: {scaled_number}")
whole_number = round(scaled_number)
print(f"whole number: {scaled_number}")
print(type(scaled_number))
print(type(whole_number))

import math
float_number = random.random()
print(f"Generated random floating number: {float_number}")
scaled_number = float_number * 50
print(f"Scaled number is: {scaled_number}")
whole_number = math.ceil(scaled_number)
print(f"whole number: {scaled_number}")
print(type(scaled_number))
print(type(whole_number))