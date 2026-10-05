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