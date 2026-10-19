# PIN with a countdown

correct_pin = "1234"
attempt = 0

while attempt < 3:
    pin = input("Enter your PIN: ")
    attempt += 1
    if pin == correct_pin:
        print("Sucess!")
        break
    elif attempt < 3:
        print(f"Wrong. {3-attempt} attempts left.")
else: 
        print("Card blocked")
