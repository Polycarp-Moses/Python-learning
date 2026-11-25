# PASSWORD CHECKER

def is_long_enough(password):
    """
    Check that a password has at least 8 characters.

    Args:
        password(str): The password to check.

    Returns:
        result(bool): True if password is long enough, otherwise False.
    """
    if len(password) >= 8:
        return True
    return False

def has_uppercase(password):
    """
    Check that a password has an uppercase letter.

    Args: 
        password(str)

    Returns:
        True or False
    """
    for letter in password:
        if letter.isupper():
            return True
    return False

def has_lowercase(password):
    """
    Check that a password has a lowercase letter.

    Args:
        password(str)

    Returns:
        True or False
    """
    for letter in password:
          if letter.islower():
               return True
    return False

def has_digit(password):
    """
    Check that a password has a digit.

    Args:
        password(str)

    Returns:
        True or False
    """
    for letter in password:
          if letter.isdigit():
               return True
    return False

def find_problems(password):
    """
    Find every rule that a password breaks.

    Args:
        password(str)
    
    Returns:
        problems(list): a list of messages, empty if the password passes all rules.
    """
    problems = []
    if not is_long_enough(password):
        problems.append("Must be at least 8 characters long")
    if not has_lowercase(password):
        problems.append("Must contain a lowercase letter")
    if not has_uppercase(password):
        problems.append("Must contain an uppercase letter")
    if not has_digit(password):
        problems.append("Must contain a digit")
    return problems

while True:
    password = input("Enter your password: ")
    problems = find_problems(password)

    if problems == []:
        print("Password accepted")
        break
    print("Password is not strong enough:")
    for problem in problems:
        print(" - " + problem)
    