# We can use "and" and "or" operators to join conditions

score = 50
submitted_project = True
if score >= 90 and submitted_project:
        print("A+")
elif score >= 90: 
     print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")