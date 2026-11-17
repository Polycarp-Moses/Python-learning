#Function Challenges
#Challenge 1
def greet(name):
    return f"Hello, {name}!"
print(greet("Maria"))

#Challenge 2
def is_even (n):
    return n % 2 == 0
print(is_even(4))
print(is_even(7))

#Challenge 3
def average(numbers):
    return sum(numbers)/len(numbers)
print(average([80,90,70]))

def average(*args):
    return sum(args)/len(args)
print(average(80,90,70))

#Challenge 4
def count_words(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
print(count_words("red blue red"))

#Challenge 5
def filter_expensive(prices, limit=100):
    expensive_prices = [
        price
        for price in prices
        if price > limit
    ]
    return expensive_prices
print(filter_expensive([50, 300, 80, 1200]))
print(filter_expensive([50, 300, 80, 1200], 500))