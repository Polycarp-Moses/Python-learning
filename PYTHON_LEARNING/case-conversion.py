# Case conversions
text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

#Use case: prevents case-based mismatches when searching data in your code or when doing comparisons

search = "Email" #say user is searching for this term
data = "email" #this is how its written in your data
print(search == data) #the output here will be "False" because they are not the same
search = "Email".lower()
data = "eMail".lower()
print(search == data)

#Best practice: clean before search. Always trimm spaces and lowercase your data and search term before matching

search = "Email " #has spaces and upper case
data = " eMail" #has spaces and uppercase
print(search == data) #output will be false
search = "Email ".lower().strip() #remove spaces and lowercase
data = " eMail".lower().strip() #remove spaces and lowercase
print(search == data) #output will be "True"