#b) While True
#This loop will run forever-it is infinite- so we add the break statement in order to force the loop to stop.

#while True: 
    #print("I am unstoppable") #This will run indefinetely without stopping

while True:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        break
print("Thank you")