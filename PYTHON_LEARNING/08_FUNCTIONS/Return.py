#RETURN
# - So far, we have focused on how data goes into our code through parameters and arguments.
# - We can extend this function by building an output from our function so that the data goes out of the function.
# - We can do this using the keyword "Return".
# - This shape of functionn is known as the Transformation Function - here, we send raw data into a function, data is transformed in the function, then this data goes out as processed data and is used in the program to do something. "Return" is used to return the result of the function to the program to be reused later. Print() is used to print something for you while Return returns something to the program.
# NB- in python, if a function has no return statement, python returns None. None in this case means that the function is not returning a real value. But if you use specify return, python sends back to the program real useful value. 
#Syntax: 
# f = 2
#def multiple_factor(x):
    # y = x * f
    # return y
# z = multiple_factor(3)
# print(z)

def clean_name(name):
    cleaned = name.strip().lower().capitalize() #here we are cleaning up the name. 
    #print(cleaned) # here previously we are printing the output, which is not something we just simply do in real projects. Rather, we use return because we need to use the cleaned value in the next steps in the code. If we leave it as it is at this point, we loose the cleaned value in the program. 
    return cleaned # here we are returning the local variable that holds the cleaned value. 
cln_name = clean_name(" MariA  ") # assign the return value - assign the function call to a variable to store the result. 
print(cln_name) # here we print the new global variable

#Note: A function can have multiple return statements
#Extend the logic: if the value is empty, convert it to None. Otherwise, clean it. 
def clean_name(Name):
    if not Name:
        return None
    else:
        cleaned = Name.strip().lower().capitalize()
        return cleaned
cln_name = clean_name("")
print(cln_name)

#Note: You can return multiple values separated by commas
#Extend the logic: Return the value in both upper and lower case
def clean_name(name):
    lo_cleaned = name.strip().lower().capitalize()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned
lo_name, up_name = clean_name(" MariA ")
print(lo_name)
print(up_name)

