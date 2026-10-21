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
#Unpacking is clean, easy, and makes code simple to extend 
person = ["Maria", 29, "Data engineer", "Spain"]
name, age, role, country = person

print(name)
print(role)

#REST COLLECTOR / ASTERICK *
#Say you are interested in the first and last items only in a list and ignore the rest?
#Put the first item in one variable and the last item in another variable, then put everything else in a single variable by applying the asterick (*) operator

person =["Maria", 29, "Data engineer", "Spain"]
name, *details, country = person
print(name)
print(details)
print(country)

print()

#Say you are interested in the first item only
person =["Maria", 29, "Data engineer", "Spain"]
name, *details = person
print(name)
print(details)

print()

#Same for the last item
person =["Maria", 29, "Data engineer", "Spain"]
*details, country = person
print(details)
print(country)

print()

#You can decide the items you want in a separate variable and those that you want to group together in a list
person =["Maria", 29, "Data engineer", "Spain"]
*details, role, country = person
print(details)
print(role)
print(country)

print()

#Only one asterik is allowed in unpacking

#Rules of Unpacking
#1. Number of variables must match the values exactly; not less, not more (if you are not using asterik)

numbers = [1, 2, 3, 4]
first, second, third, last = numbers
print(first)

print()

#2. Asterik collects leftovers, and its fine if there are none

numbers = [1]
first, *rest = numbers
print(first)
print(rest)

print()

#3. You can unpack any sequence (lists, tuples, strings, etc.)

word = "Hi"
first, *rest = word
print(first)
print(rest)

print()


#SKIPPING ITEMS - UNPACKING USING UNDERSCORE("_")
#Allows you to skip naming variables and values that you don't need to unpack
#Useful when you don't have a lot of data in a list

learner = ["Python", 34, "Nairobi", "Software Engineer"]
language, _, city, _ = learner
print(language)
print(city)

print()

#You can combine use of asteriks and underscores
#Discards everything else that you don't want to unpack
learner = ["Python", 34, "Nairobi", "Software Engineer"]
language, *_, country = learner
print(language)
print(country)



