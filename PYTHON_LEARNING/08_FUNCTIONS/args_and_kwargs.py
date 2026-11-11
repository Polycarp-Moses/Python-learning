# *args & **kwargs
# So far we have defined the exact number of parameters and arguments for our functions. 
# But sometimes you don't know in advance how many arguments will be passed to your function. 
# *args and **kwargs allow functions to accept a unknown number of arguments.
# - *args accepts multiple positional arguments - only values
# - **kwargs accepts multiple keyword arguments - names and values
# - *args - used when passing the same type of information
# - **kwargs -used when passing different types of information
# *args- stores data as tuples while **kwargs store data as dictionaries(key:value pairs)

#calctulate the total of values
def total(*args): #we are telling the function here to accept any number of arguments
    print(type(args)) #args belongs to the class tuple, which means we can use any functions and methods from tuple such as sum()
    print(sum(args)) 
total(1,2)
total(1,2,3)
total(1,2,3,4) # we can pass any number of arguments

#When to use *args: 
# - when you pass similar values e.g a list of numbers [1,2,3,4,5], or multiple string values (Alex, Moses, Morgan, Humphrey)
#When to use **kwargs:
# - when you pass different types of values e.g. (Alex, 25, alex@gmail.com), 11.11.2026

#Create the user profile:
def create_user(**kwargs):
    print(type(kwargs)) # kwargs are dictionaries because we use keyword arguments, which are key:value pairs
    print(kwargs)
create_user(first_name = "Bukayo",
            last_name = "Saka",
            age = 27,
            country = "England") #**kwargs only work with keyword arguments
create_user(name = "Ronaldo", country = "Portugal")