# Age and ticket pricing

age = int(input("Enter your age:"))
if age < 0 or age > 120:
    print("Invalid age")
elif  age < 5:
    print("Your ticket is free")
elif age <= 17:
    print("Ticket price is 300 ksh")
elif age <= 59:
    print("Ticket price is 500 ksh")
else:
    print("Ticket price is 250 ksh")