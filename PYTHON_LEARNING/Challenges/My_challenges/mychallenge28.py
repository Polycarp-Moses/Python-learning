#While True challenges

#Challenge 1
def type_something():
    while True:
        something = input("Type something (or quit): ")
        if something == "quit":
            break
        else:
            print(something.upper())
type_something()

#challenge 2
def enter_age():
    while True:
        age = input("How old are you?")
        if age.isdigit():
            age = int(age)
            if age >= 1 and age <= 120:
                print(f"Thanks you are {age}")
                break
        print("Please enter a whole number from 1 to 120")
enter_age()

#challenge 3
def add_numbers():
    total = 0
    while True:
        entered_number = input('Enter number or "done": ')
        if entered_number == "done":
            print(f"total: {total}")
            break
        total = total + int(entered_number)
add_numbers()

