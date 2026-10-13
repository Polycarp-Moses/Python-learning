#Print the numbers 1 to 10 with even or odd next to each other

for number in range(1,11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")