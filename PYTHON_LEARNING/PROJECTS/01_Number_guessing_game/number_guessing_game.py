# NUMBER GUESSING GAME
import random

def get_guess():
    while True:
        guess_text = input("Enter your number: ")
        if guess_text.isdigit():
            return int(guess_text)
        print("Please enter a whole number.")

def play_game():
    
    secret_number = random.randint(1,100)
    max_attempts = 7
    attempts = 0
    while attempts < max_attempts:
        your_guess = get_guess ()
        attempts += 1
        if your_guess < secret_number:
            print(f"Too low, {max_attempts-attempts} attempts left")
        elif your_guess > secret_number:
            print(f"Too high, {max_attempts-attempts} attempts left")
        else:
            print("Correct!")
            break
    else: 
        print(f"Game over! The number was {secret_number}")
play_game()