# whitespace cleanup
#lstrip
text = " Engineering"
print(text)

text = " Engineering".lstrip() #remove space before "Engineering"
print(text)

#rstrip
text = "Python "
print(text)
text = "Python".rstrip() #remove spaces from the right side
print(text)

#strip
text = " Python "
print(text)
text = " Python ".strip() #removes all extra spaces from both ends
print(text)

#Remove any characters you want
text = "####ABC###"
print(text)
text = "####ABC###".strip("#")
print(text)

#use case: Check length before and after strip() to find unwanted spaces
text = "Engineering"
print(len(text)) #check the length of value
print(len(text.strip())) #check the length of value after applying strip method

print(len(text) - len(text.strip())) #check the number of problems in your data
print(len(text) == len(text.strip())) #compare if lenth of original data is equal to lengh after strip()

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Number of spaces:", nr_of_spaces)
print("Is my data clean?", is_clean)