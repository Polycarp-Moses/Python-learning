# Grade calculator

score = int(input("Enter your score:"))
if score < 0 or score > 100:
    print ("Invalid score")
elif score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")