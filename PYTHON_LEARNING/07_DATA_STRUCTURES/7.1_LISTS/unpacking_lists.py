#UNPACKING LISTS
#Involves unpacking and putting different types of data in different variables, so that we can apply different operations.

person =["Maria", 29, "Data engineer", "Spain"]
#Without unpacking, using only indexes makes code long and hard to extend as seen below
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

#Unpacking utilizes list of variables, separated by commas
#Order of variable names must match the order of the list values
name, age, role, country = person

print(name)
print(role)

#Unpacking is clean, easy, and makes code simple to extend