#Each data structure behaves differently in python
#These behaviours can be categorized into 4 characteristics: ordered, duplicate, indexed, mutable

#LISTS
#-Ordered
# - python remembers the order of your list. Order changes when you change it.
scores = [10, 20, 30, 40]
print(scores) #ordered

#Duplicates
# - In python, lists allow duplicates- you can store the same value more than once
scores = [10, 20, 30, 40, 10] #allows 10 to be duplicated
print(scores)

#Indexed
#-Lists are indexed- you can use position number of your values to access the values
scores = [10, 20, 30, 40]
print(scores[1])

#Mutable
#-After creating your list, you can go ahead and change it by adding, remvoving, inserting, updating, sorting the values
scores = [10, 20, 30, 40]
scores[3] = 77
print(scores)