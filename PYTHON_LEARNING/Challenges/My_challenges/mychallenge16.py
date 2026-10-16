#Guessing game; the secret number is 7. Keep asking untill the user guesses it, count the guesses, then print "You got it in x attempts"

secret_number = 7
attempts = 0
while True:
    guess = int(input("What's your guessed number? "))
    attempts += 1
    if guess == secret_number:
        break
print(f"You got it in {attempts} attempts")
