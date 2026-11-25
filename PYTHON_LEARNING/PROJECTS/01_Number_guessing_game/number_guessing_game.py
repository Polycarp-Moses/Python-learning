# NUMBER GUESSING GAME
import random

def get_guess() -> int:
    """
    Ask the player for a guess until a valid whole number is entered. 
    Returns:
        guess(int): The player's guess.
    """
    while True:
        guess_text = input("Enter your number: ")
        if guess_text.isdigit():
            return int(guess_text)
        print("Please enter a whole number.")

def check_guess(guess: int, secret_number: int) -> str:
    """
    Compare a guess with the secret number.
    Args:
        guess(int): The player's guess.
        secret_number(int): The number the player is trying to find.
    Returns:
        result(str): "low", "high" or "correct".
    """
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"

def play_game(max_attempts: int = 7) -> None:
    """
    Play one round of the number guessing game. 
    Args: 
    max_attempts(int): How many guesses the player gets. 
    """
    
    secret_number = random.randint(1,100)
    attempts = 0

    while attempts < max_attempts:
        guess = get_guess ()
        attempts += 1
        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f"Correct! You got it in {attempts} tries.")
            break
        else:
            print(f"Too {result}, {max_attempts-attempts} attempts left")
    else: 
        print(f"Game over! The number was {secret_number}")
play_game()