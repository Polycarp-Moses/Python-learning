#We have two boolean operators: True/False
print(True)
print(False)
print(type(True))

#functions that return True or False
#bool(value)
print(bool(123)) #checks if you have an empty or real value
print(bool("Hi"))
print(bool()) #returns false because it is an empty value
print(bool(0)) #also returns false becaue zero is considered an empty value
print(bool("")) #also empty
print(bool(None)) #also considered to be empty

#any() and all() Functions

email = "mosekamau007@gmail.com"
phone = "0705097054"
username = ""
#say you have a website that allows registration
#if any field is filled
print(any([email,phone,username]))

#only if all fields are filled
print(all([email,phone,username]))

#isinstance(value,type): builtin function that checks if a value belongs to a certain data type. outputs boolean

print(isinstance(123, int))
print(isinstance(True, str))

#endswith(substring) -string method that checks if the string ends with a specific word. outputs bool

print("hello".endswith("o"))
print("hello".startswith("o"))