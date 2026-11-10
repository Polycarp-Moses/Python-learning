# POSITIONAL AND KEYWORD ARGUMENTS
# In real projects, we don't usually work with one or a single parameter(input); rather we usually work with multiple parameters and multiple arguments.
#So how do we go about the order of the arguments?

#Example: 1. send both first and last name to be cleaned. 2. Merge them into a full name.
def clean_name(first_name, last_name, country):
    first = first_name.strip().lower().capitalize()
    last = last_name.strip().lower().capitalize()
    full_name = first + " " + last
    print(full_name, "From", country)
clean_name(" MariA  ", "SMITH", "DE")
clean_name("KAMAU", "MOSES", "KE")

print()

#Keyword Arguments and Positional Arguments
#In python we have two different ways in which we can send values to the function. The two ways are called positional argumnets and kewyord arguments.
# Positional arguments - are values passed to he function based on their ORDER
# Keyword arguments - values passed to the function based on their NAMES

# We have used posisitional arguments in this example:
# Positional argument rule: the order of arguments must match the order of the parameters
def clean_name(first_name, last_name, country):
    first = first_name.strip().lower().capitalize()
    last = last_name.strip().lower().capitalize()
    full_name = first + " " + last
    print(full_name, "From", country)
clean_name(" MariA  ", "SMITH", "DE") #positional
clean_name("KAMAU", "MOSES", "KE") #positional

print()

#keyword arguments:
# The order in keyword arguments doesn't matter which is major advantage compared to positional arguments.
# Readability: keyword arguments are easier to read and understand than positional 
# Safety: keyword arguments are safer since they reduce mistakes with clear names
# overhead: keyword arguments take more time to write and maintain
def clean_name(first_name, last_name, country):
    first = first_name.strip().lower().capitalize()
    last = last_name.strip().lower().capitalize()
    full_name = first + " " + last
    print(full_name, "From", country)
clean_name(country = "KE", first_name= "bARACK", last_name= "obama") #keyword. 
clean_name(first_name= " JohN  ", last_name= "SMITH", country= "USA") #keyword

#Positional vs keyword: which one do you choose?
# Depends on the number of parameters
# 2-3 parameters - use positional arguments
# More than 3 parameters - use key word arguments
