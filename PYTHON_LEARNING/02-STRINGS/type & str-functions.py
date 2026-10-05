name = "Moses"
print(type(name))

age = 34
print(type(age))
#print("Your age is: " + age) -will return an error because you can't combine a string with an integer using + operator. can only work if you have two int or two strings

print("Your age is: " + str(age))

age = age + 5 #this will work because age is number and 5 is number
print("age: ", age)

age = str(age) #changing the value of age to be a string and assigning it again to age
print(type(age)) #returns string data type
#age = age + 5 -here now you will get an error because age at this point is a string


