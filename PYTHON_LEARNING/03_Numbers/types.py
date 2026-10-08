# How to check type of the numeric values
x = 5
y = 5.7
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

#How to convert data types to numeric data types
x = "24"
print(type(x))
x = int(x)
print(type(x))
print(x*4)

#Converting float into an int(whole number)
x = 3.14
print(int(x))

#converting int into float
x = 3
print(float(x))

#convert string into float
x = "3.14"
print(float(x))

# converting values into complex numbers
x = 3 #real part
y =4 #advanced part
print(complex(x,y))