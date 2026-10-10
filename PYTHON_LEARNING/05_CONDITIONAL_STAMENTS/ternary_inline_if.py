#Inline if statement A.K.A Ternary Operator
# "A" if score >= 90 else "F"
#Used for simple logic

score = 90

grade = "A" if score >= 90 else "F"
print(grade)

# What if we have an else if
grade = "A" if score >= 90 else "B" if score >=80 else "F"
print(grade)
