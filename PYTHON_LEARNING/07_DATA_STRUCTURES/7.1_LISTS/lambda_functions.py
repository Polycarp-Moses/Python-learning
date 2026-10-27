#LAMBDA FUNCTIONS
#Used to create quick, custom logic
#Lambda functions are tiny functions withou a name
#They are also known as anonymous functions
#They are a one line function
#syntax: output(variable name) = lambda x(input): Expression

multiple = lambda x: x*2 #variable(multiple)-stores a lambda function which doubles a number
print(multiple(2))

#You can have two inputs
add = lambda x, y: x+y
print(add(1, 2)) #when lambda has two parameters, you must pass two values when calling it

#A lambda can contain any expression, including conditions
check = lambda i: i in "python"
print(check("n"))

#Lambda + Map
#Task: Prices are stored as messy strings and need cleaning to floats
prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))