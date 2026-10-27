#LIST COMPREHENSIONS
#You can combine data transformation, loops and data filtering

#Task: Normalize the domains into standard format
domains = ['www.google.com', 'openai.com', 'localhost', 'www.DATAWITHBARAA.COM']
cleaned = [
    domain.lower().replace('www.', '') #data transformation
   for domain in domains #For loop - don't use colons
    if '.' in domain #Data filtering -if this is true then do the transformation
]
print(cleaned)