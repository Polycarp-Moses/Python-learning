#Validate the quality and correctness of passwords
#Must not be empty
#Must be at least 8 characters 
#Must include at least 1 uppercase
#Must include at least 1 lowercase
#must not be the same as email
#must not contain any spaces
#must start and end with a letter or digit

password = "Mosekamau00@"
email = "Mosekamau@gmail.com"
password = password.strip()
#Must not be empty
if password == "":
    print("Password cannot be empty")
#Must be at least 8 characters 
elif len(password) < 8:
    print("Password must be at least 8 characters")
#Must include at least 1 uppercase
elif password == password.lower():
    print("Password must contain at least 1 uppercase")
#Must include at least 1 lowercase
elif password == password.upper():
    print("Password must contain at least 1 lowercase")
#must not be the same as email
elif password == email:
    print("Password must not be same as email")
#must start and end with a letter or digit
elif not(password [0].isalnum() and password [-1].isalnum()):
    print("Password must start and end with a letter or digit")
else: 
    print("Password is valid")