#Syntax:
i = 1 #initialization-defines the initial value of the loop variable
while i < 4: #condition
    print(i)
    i+=1 #update-changes the value that you are checking inside your condition
print()

#Use case: building a counter that counts from 1 to 5:
count = 1 #initialization
while count <= 5: #condition
    print(count)
    count +=1 #update 

print()

#use case: Write a program that keeps asking "Do you agree?", until the user types "yes"
answer = ""
while answer != "yes":
    answer = input("Do you agree? (yes/no): ")
print("Thank you")