# FUNCTION TYPES - BY PURPOSE
#So far we have covered types of functions based on how data flows through the functions. e.g no input/output, only input, input and output with parameters, arguments and return, and multi inputs and outputs.
# In real projects, we also categorize functions by purpose (use cases) or jobs that they are responsible for.

# 1. ACTION FUNCTIONS (A.K.A Side Effect functions, Command functions, Handler functions, Service functions)
# - Designed to perform an operation in the system instead of returning values. 
# - They are focused on side effects - they change something outside the function. 
# - Examples: functions that print something on the screen, functions that save data to a file/database, functions that send emails or notifications if something goes wrong, or functions that call an external API. 

# TASK: Stores application log messages in a file whenever an event occurs. 
# "with open" -keyword that opens the file safely and closes it automatically when done 
# - "C:\users\Administrator\Desktop\Python-learning\app.log" - speficies the path of the file - python will create a file called "app.log" inside this path (C:\users\Administrator\Desktop\Python-learning\app.log)
# - "r" tells python that this is a string and not a special character backslash(\) 
# - "a" -tells python how to store the information inside the file- append mode "a" appends data/messages at the end of the file - tells python to append the message and not to delete or update it. 
# -  file.write(message + "\n") - is the action - tells python we are writing inside the file by adding a parameter message into a new line- in short this means we are writing something(message) to the file and each message should be in a new line

def write_log(message):
    with open (r"C:\users\Administrator\Desktop\Python-learning\app.log", "a") as file:
        file.write(message + "\n")

write_log("App Started") #if the program runs from the start, this indicates the first event
write_log("User logged in")
write_log("App stopped")

# 2. TRANSFORMATION FUNCTIONS(A.K.A data functions, calculation functions, utility functions, mapper functions)
# - Function that gets raw data as an input, transforms the data, and returns processed data.
# Examples of such transformations can including calculating new values, transforming a text or structure, extracting or reshaping data e.t.c

#TASK: clean email addresses and split them into structrured data (username and domain)

def clean_and_split_email(email):
    cln_email = email.strip().lower()
    # SAra@gmail.COM
    username, domain = cln_email.split("@") #.split() method splits the text at the speficied place
    return {"username": username, "domain": domain} #returns as a dictionary in key:value pairs
cleaned = clean_and_split_email(" SAra@gmail.COM ") #assign to a global variable
print(cleaned)

# 3. VALIDATION FUNCTIONS(A.K.A Checker functions)
# - Validates a condition and returns a boolean result (True or False)
# - Validation functions are more focused on rules and correctness more than changing your data or program.
# Useful in:- checking user input, checking business rules, checking data quality and checking user permissions. 

#TASK: Check whether the password meets the minimum requirement of 8 characters
def is_valid_password(password):
    return len(password) >= 8 #check using len() then return the result of the check
print(is_valid_password("123456"))
print(is_valid_password("1234568883"))

#TASK: Check whether an email address has a basic valid format
def is_valid_email(email):
    return "@" in email and "." in email
print(is_valid_email("mosekamau.com"))
print(is_valid_email("mose@kamau.com"))

# 4. ORCHESTRATOR FUNCTION (A.K.A controller functions, pipeline functions, workflow functions, cordinator functions, e.t.c)
# - Controls program flow by calling other functions in the correct order. 
# - They are focused on coordination rather than changing data or the logic. Their main work is to connect everything together and to decide the next step to be executed or the next function to be called. 

# TASK: 
# 1. Receive an email
# 2. Validate the email.
# 3. If is it invalid, Log an error in a file
# 4. If it is valid, clean and structure the email.
# 5. Log each step of the program. 

def process_user_email(email):
    write_log("App Started")
    #we must check if it is vali, if it is not valid, we log the problem
    if not is_valid_email(email):
        write_log(f"Invalid Email Received: {email}")
    #if it is valid, we clean it and store structured information
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")
    write_log("App stopped")
#we receive an email from a user
email = input("Please enter your Email: ")
process_user_email(email)