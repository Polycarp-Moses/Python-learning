#DICT METHODS

#Access - you can use keys to access values
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
print(user['city'])

#If the key is not found, python throws a KeyError. So instead use get()
#get() -returns the value safely, gives None if missing
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
print(user.get('name'))
print(user.get('age'))

#get () - missing keys return None or your default value
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
print(user.get('name', 'unknown')) #'unknown' passed here as the default value

# in operator - tests if the key is inside the dictionary
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
print('age' in user)
print('name' in user)
print('name' not in user)

#View Objects - these objects give you a live view of the dictionary's keys, values, or key value pairs - they give you insights about the structure of your dict

# 1. keys() - returns all trhe KEYS in you dictionary
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
print(user.keys())

# 2. values() - returns all the VALUES in your dict
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
print(user.values())

# 3. items() - returns all (key, value) pairs of your dict - perfect when you need key and value together for looping, transforming data, building new dicts, comparing and more
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
print(user.items())

#Looping example
for key, value in user.items():
    print(key, value)

# ADD, REMOVE, UPDATE
# Assign key - updates the value if the key exist, or inserts a new key value pair if it doesn't
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
user['name'] = 'Moses' #add
user['id'] = 3 #update
print(user)

#update()- updates multiple values- adds new keys and updates exisiting ones using anotrher dictionary
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
user.update({'age': 40, 'city': 'Paris'})
print(user)

#pop() - removes a key from the dict and returns its value
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
#user.pop('age')
age = user.pop('age') #pop returns the value of the removed item; so you can go ahead and store it in a variable
print(user)
print('Removed item:', age)

#pop() removes the key and returns its value, or returns your default if the key is missing
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
salary = user.pop('salary', 'Not Found')
print('Removed item:', salary)

#popitem() - returns and deletes the most recent key value pair from the dictionary
user = {'id': 1, 'age': 34, 'city': 'Nairobi'}
user.popitem()
print(user)

#fromkeys() - builds a new dictionary where all keys get the same default value
user = dict.fromkeys(['id', 'name', 'age', 'city'], None)
print(user)