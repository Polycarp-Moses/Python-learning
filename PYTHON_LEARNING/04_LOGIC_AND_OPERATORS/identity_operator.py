#Identity (is) Operator - checks if two variables refer to the same object in memory

x = ["a", "b", "c"]
y = ["a","b", "c"]

print(x == y) #This will return True because we are comparing the values
print(x is y) #This will return False because python creates a separate object for each variable with different IDs

x = 10
y = 10

print(x == y)
print(x is y) #This will return True because this is a simple value, which python will optimize the two values of the variables and put them in one object

# "=" between two variables assigns one variable to the same object that another variable is referring to

x = ["a", "b", "c"]
y = x

print(x == y)
print(x is y)

#Use case: validate the email address exists. It must be filled in and not empty

email = "" #"" means an empty but it is known, it is string
print(email != "")

email = "mosekamau007.gmail.com"
print(email != "")

email = None #None means no value at all, it is unknown
print(email != None and email != "")

#Use is instead of == when checking None. Its good practice

email = None 
print(email is not None and email != "")