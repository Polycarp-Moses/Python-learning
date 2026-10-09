#Nested if
#Simply means putting if statements inside another if statement.
#If the first is true, then check the second

score = 95
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else: 
     print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")