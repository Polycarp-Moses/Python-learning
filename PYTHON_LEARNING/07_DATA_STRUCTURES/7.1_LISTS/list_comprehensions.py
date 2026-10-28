#LIST COMPREHENSIONS- a shortcut for a for loop that builds a new list
#You can combine data transformation, loops and data filtering
#Syntax: 1. What goes into the new list? 2. Where do the items come from? (for item in items) 3. Do i need a check?(if...)
#Task: Normalize the domains into standard format
domains = ['www.google.com', 'openai.com', 'localhost', 'www.DATAWITHBARAA.COM']
cleaned = [
    domain.lower().replace('www.', '') #data transformation
    for domain in domains #For loop - don't use colons; 
    if '.' in domain #Data filtering -if this is true then do the transformation
]
print(cleaned)

# How python runs the code above:
# 1. for domain in domains: take each item one at a time
# 2.  if '.' in domain: does it pass the check? 'localhost' has no dot, so it is thrown away
# 3. domain.lower().replace('www.', ''): clean the items that passed and put the result in the new list

#Task: Make a list of the names that start with 'M' written in capital letters
names = ['maria', 'kumar', 'max', 'anna']
cleaned = [
    name.upper()
    for name in names
    if name.startswith('m')
]
print(cleaned)

#Task: Make a list of each number times 10, but only for numbers bigger than 3.
numbers = [1,2,3,4,5,6]
new_list = [
    number * 10
    for number in numbers
    if number > 3
]
print(new_list)

#Task: Make a list of the lengths of each word.
words = ['hi', 'python', 'sql', 'code']
new_list = [
    len(word)
    for word in words
]
print(new_list)

#Task: Make a list of only the prices under 100
prices = [120, 45, 300, 80]
new_prices = [
    price
    for price in prices
    if price < 100
]
print(new_prices)

#Task: Make a list of each name with the first letter capitalized.
names = ['maria', 'kumar', 'max']
new_names = [
    name.capitalize()
    for name in names
]
print(new_names)

#Make a list of only the words longer than 3 letters, written in capitals
words = ['hi', 'python', 'sql', 'code']
new_words = [
    word.upper()
    for word in words
    if len(word) > 3
]
print(new_words)