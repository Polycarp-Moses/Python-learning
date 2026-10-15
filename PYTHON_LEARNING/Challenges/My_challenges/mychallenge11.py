#Login system

correct_username = "moses_kamau"
correct_password = "mudha1"

entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

if entered_username.lower() != correct_username:
    print("User not found")
elif entered_password != correct_password:
    print("Incorrect password")
else:
    print("Welcome!")