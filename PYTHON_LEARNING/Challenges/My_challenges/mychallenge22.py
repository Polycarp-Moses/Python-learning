# #Name check
# while True:
#     name = input("Enter your name:").strip()
#     if name != "":
#         break
# print(name)

# #Shopping total
# total = 0
# while True:
#     price = (input("Enter the price (or 'done'): "))
#     if price == "done":
#         break
#     total += int(price)
# print(f"The total is: " ,total)

#Guess with hints
count = 0
while True:
    guess = int(input("Enter your guess: "))
    count += 1
    if guess == 7:
        break
    elif guess < 7:
        print("Too low")
    elif guess > 7:
        print("Too high")
print(f"You got in {count} guesses")