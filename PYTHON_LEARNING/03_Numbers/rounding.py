# Measure distance
#print(2-8) #the result here will be a negative number
print(2-8)
print(abs(2-8)) #abs () function will return the absolute (non-negative) value of a number - used for measuring distance or size, regardless of direction

import math
#Rounding Numbers
price = 23.543983
print(round(price))
print(round(price,2)) #rounds number to the specified number of decial places
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price)) #cuts off the decimal part and keeps the whole number (no rounding)