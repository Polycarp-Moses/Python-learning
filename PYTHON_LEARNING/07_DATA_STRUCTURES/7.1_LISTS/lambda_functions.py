#LAMBDA FUNCTIONS
#Used to create quick, custom logic
#Lambda functions are tiny functions without a name
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
print(list(map(lambda p: float(p.replace('$', '')), prices))) #start by data transformation by using p.replace() to remove the dollar sign, then use float() to change data type from string to float, then put the formula "float(p.replace('$', ''))" in a lambda, then use the map function to apply it in all items in the list, then change the data type using list(), then print  

print()

#Lambda + Filter(function, iterable)
#Instead of passing the built in functions to Filter(), we can pass our custom special functions by using lambda
#filter(lambda input: expression, iterable)
#Task: remove all prices lower than 100
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))
#first write the logic: p >= 100
#Now use lambda to create the function: lambda p: p >= 100
#Then use filter function to filter the unwanted data: filter(lambda p: p >= 100, prices)
#Then change the data type: list(filter(lambda p: p >= 100, prices))
#Then print.

#Task: Keep only students with scores higher than 70
students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]
print(list(filter(lambda row: row[1] > 70, students)))
print()
#matrix iteration happens one row at a time
#First check what you are selecting and create logic: students[0][1] > 70
#Then put it in lambda; input will be the whole row: lambda row: row[1] > 70
#Then use filter: filter(lambda row: row[1] > 70, students)
#Then convert data type: list(filter(lambda row: row[1] > 70, students))
#Then print.

#Task: Keep only students with names starting with 'M'
students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]
print(list(filter(lambda row: row[0].startswith('M'), students)))

#Task: Keeps the scores of 60 or more
scores = [45, 80, 62, 91]
print(list(filter(lambda score: score >= 60, scores)))
print(list(map(lambda score: score + 5, scores)))