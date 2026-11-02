#DICTIONARIES
#Data structure that helps you store multiple types of values in one place. e.g customer name, age, country etc
#A dictionary helps you store different types of information in key-value pairs; where the key describes what the data means or the description of the data and the value holds your actual data
#syntax: customers = {Name: Moses, Age: 34, Country: Kenya}
#Dict behaviors:

# 1. dict is ordered
my_dict = {'a': 10, 'b': 20, 'c': 30}
print(my_dict)

# 2. Keys must be unique - no duplicates, but values allow duplicates
my_dict = {'a': 10, 'b': 20, 'c': 30, 'a': 40, 'b':20}
print(my_dict)

# 3. dict is not indexed
my_dict = {'a': 10, 'b': 20, 'c': 30}
#print(my_dict[1])

# 4. Instead you access values by using keys, not indexes - dict is keyed
my_dict = {'a': 10, 'b': 20, 'c': 30}
print(my_dict['b'])

# 5. Dict is mutable
my_dict = {'a': 10, 'b': 20, 'c': 30}
my_dict['c'] = 80
print(my_dict)