#Email Validator

email = input("Enter your email:")

if email == "":
    print("Email is invalid")
elif email.count("@") != 1:
    print("Email must contain  exactly one @")
elif " " in email:
    print("Email must not contain spaces")
elif not email.endswith((".com", ".co.ke")):
    print("Email must end with .com or .co.ke")
elif email[0] == "@":
    print("Email must have one character before @")
else: 
    print("Your email is valid")