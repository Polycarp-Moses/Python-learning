# Password loop

while True:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password is too short")
        continue
    has_upper = False
    for letter in password:
        if letter.isupper():
            has_upper = True
    if not has_upper:
        print("No uppercase letter")
        continue
    break
print("Password accepted")