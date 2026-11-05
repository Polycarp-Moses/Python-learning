#USER-DEFINED FUNCTIONS
#How they work?
#User-defined functions have two parts - the function definition(declaration) and the function call. 
# Function definition is where you describe the function or what the function should do. Syntax: def function_name(): # below it after the collons you have your block of code, such as assigning values to variables, loops, conditional statements or even calling another built in function. 
# Function call is how you use the function. Here you just write the function name; i.e function_name() -once python sees it, it will execute the function. 
# If you define a function, python creates an object in your memory to store your function, and you only get an output when you call the function. 

#Example of a simple user-defined function:
def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add milk")
    print("Enjoy it")
print("wake up")
make_coffee()
print("work for a while")
make_coffee()