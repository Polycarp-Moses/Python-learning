#Validate the quality and correctness of email values (5.11)
# Email must not be empty
# Email must concom, .org or .nettain a "." and "@"
#Email must contain exactly one "@" symbol
#email must end with .com, .org or .net
#Email must not be longer than 254 characters
#Email must start and end with a letter ot digit


email = "mosekamau007@gmail.com"
email = email.strip() #() strip removes leading and trailing and whitespaces from a string
if email == "":
    print("Email cannot be empty")
# Email must contain a "." and "@"
elif not( "." in email and "@" in email): #use in and not operators
    print("Email must contain . and @")
#Email must contain exactly one "@" symbol
elif email.count("@") != 1: # count () method counts how often a specific value shows up in a string
    print("Email must contain exactly one @")
#email must end with .com, .org or .net
elif not email.endswith(('.com', ',org', '.net')):
    print("Email must end with .com, .org or .net")
#Email must not be longer than 254 characters
elif len(email) > 254: #len() returns the numbe of characters in a string
    print("Email must not be longer than 254 characters")
#Email must start and end with a letter ot digit
elif not(email [0].isalnum() and email [-1].isalnum()): #isalnum()-checks if the string contains only letters and digits
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid")
