#Indexes  and Slicing
#Indexing

text = "Python"

#Extract the first character
print(text[0]) #positive index

print(text[-6]) #negative index

#Extract the last character
print(text[5]) #positive index

print(text[-1]) #negative index

#Extract 'h'
print(text[3])
print(text[-3])

#Slicing
date = "2026-10-03"

#Extract the year
print(date[0:4])
print(date[:4]) #open-ended slicing: if you leave the start index empty, python starts from index 0

#Extract the Month
print(date[5:7])

#Extract the day
print(date[8:])
print(date[-2:]) #negative index
