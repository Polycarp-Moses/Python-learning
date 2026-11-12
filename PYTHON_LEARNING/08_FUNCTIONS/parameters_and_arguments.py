#FUNCTION SHAPES:
#- Functions work differently - there are those with no input nor ouput; those with only input no output, those with input and output and those with multiple inputs and multiple outputs.
# -Data that goes in through an input is called PARAMETERS and ARGUMENTS and data that goes out is called RETURN VALUE.

#PARAMETERS AND ARGUMENTS:
# Parameters - are names used in function definition that describes what data the function expects
# Arguments - are the actual values passed in a function call that are assigned to parameters
# Syntax: 
#      def function_name(Parameter)
#      body/lines of code
#      function_name(Argument)
# Parameters vs Arguments: Parameters are used in the fucntion definition while Arguments are used in the function call; Parameters are the placeholders while the arguments are the real values that fill the placeholder; parameters define what the function expects(defines the input) while arguments provides the data/values that go inside the function.

#Example:
name = " MariA  "
print(name.strip().lower().capitalize(), "\n") # Since we always have inconsisent strings or texts in our code, we can put this logic inside a function so that we use it over and over in our code. (Rule: Always normalize strings first when transforming data)

# We create a function that works with any value- value changes but the logic stays the same.
def clean_name(name):
    print(name.strip().lower().capitalize(), "\n")
clean_name(" MariA  ")
clean_name("KAMAU")
clean_name("morGAN")

# #PARAMETERS - LOCAL VARIABLES - GLOBAL VARIABLES
# # Global variable - created outside the function and can be accessed anywhere.
# # Local variable - created inside the function and can be accessed only inside the function. 
# # Bts: The global variable has the longest lifespan; it is created at the start of the program and lives until the program ends. The local variable and the parameter have the shortest lifespan; it is created when the function starts and is destroyed when the function ends.

# # Syntax:

f = 2 #global variable
def multiple_factor(x): #function def; parameter x
    y = x * f #local variable
    print(y, "\n")
multiple_factor(3) # function call; 3 is the argument
print(f) #global variable can be accessed anywhere
#print(y) # local variable can only be accessed inside the function. 
#print(x) # Parameter can only be accessed inside the function
# NB: Raw vs Processed data - parameter keeps the raw value to be reused; local variable holds the processed version

def clean_name(name): #parameter
    cleaned = name.strip().lower().capitalize() #local v
    print("Raw:", name)
    print("Cleaned:", cleaned)
clean_name(" MoSeS")

# Control logic globally - a global variable controls behavior without changing the function

case_rule = "n/a" # global variable
def clean_name(name): #parameter
    cleaned = name.strip() #local variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned:", cleaned)
clean_name(" MoSeS")
print("The rule is:", case_rule) # Global access: a global variable is available across the entire script