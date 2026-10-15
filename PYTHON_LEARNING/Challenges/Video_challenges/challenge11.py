#Allow upto 3 attempts
#If the user types "yes" print "Glad we are on the same page"
#Otherwise, print "3 strikes, You are out"
attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ") 
    if answer == "yes":
        print("Glad we are on the same page")
        break
    attempts += 1
else:
    print("3 strikes, you are out!")