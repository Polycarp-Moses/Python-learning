#Challenge: keep only string values and convert them to uppercase
# 1. Create new dict
# 2. keep only pairs with string values
# 3. convert values to uppercase
# 4. elegant and short solution
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}
new_dict = {
   k: v.upper()
    for k, v in user.items()
    if isinstance(v, str)
}
print(new_dict)

print()

#challenge: change a dict
stock = {"apples": 10, "bananas": 0, "oranges": 5}
stock.update({"apples": 15, "mangoes": 8})
stock.pop("bananas")
print(stock)

print()

#challenge: loop and print; print one sentence per person
ages = {"Maria": 25, "Kumar": 31, "Max": 19}
for k, v in ages.items():
    print(f"{k} is {v} years old")

print()

#challenge: build a dictionary that counts how many times each word appears
words = ["red", "blue", "red", "green", "blue", "red"]
new_dict = {}
for word in words:
       new_dict[word] = new_dict.get(word, 0) + 1
print(new_dict)

print()

#challenge: keep only those that cost less than 100
prices = {"pen": 50, "book": 300, "bag": 1200, "ruler": 80}
new_prices = {
      k:v    
      for k, v in prices.items()
      if v < 100
}
print(new_prices)

print()

#Challenge: double every price:
prices = {"pen": 50, "book": 300, "bag": 1200, "ruler": 80}
new_prices = {
      item:price*2
      for item, price in prices.items()
}
print(new_prices)

#challenge: swap keys and values: make a new dictionary where the numbers are the keys
letters = {"a": 1, "b": 2, "c": 3}

#loop version:
new_dict = {}
for k, v in letters.items():
    new_dict[v] = k
print(new_dict)

#comprehension version:
new_dict = {
     v:k
     for k, v in letters.items()
}
print(new_dict)

print()
#challenge: dictionary to list: make a list (not a dictionary) of the names whose score is above 70
scores = {"Maria": 85, "Kumar": 70, "Max": 60}
new_list = [
     name
     for name, score in scores.items()
     if score >= 70
]
print(new_list)

print()

#challenge: from the user dictionary, keep only the pairs where the value is a number(int), and add 1 to each one
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}
new_user = {
     k:v + 1
     for k, v in user.items()
     if isinstance(v, int)
}
print(new_user)