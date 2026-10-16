#Password with 3 tries: the correct password is "python123". Give 3 attempts. If its right, print "Access granted" and stop. If all 3 are wrong, print "Locked out".

correct_password = "python123"
attempts = 0
while attempts < 3:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted")
        break
    attempts += 1
else:
    print("Locked out")