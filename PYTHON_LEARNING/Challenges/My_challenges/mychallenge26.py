#Challenge: Dict to list: make a list of the items that are out of stock(the value is 0)
inventory = {"pen": 10, "book": 0, "bag": 4, "ruler": 0}
new_list = [
    item
    for item, price in inventory.items()
    if price == 0
]
print(new_list)

print()

#challenge: count how many times each letter appears in "banana"
word = "banana"
letters = {}
for letter in word:
    letters[letter] = letters.get(letter, 0) + 1
print(letters)

#comprehension version
word = "banana"
letters = {
    letter: word.count(letter)
    for letter in word
}
print(letters)

print()

#Two lists into one dictionary: make one dictionary that matches each name to its age
names = ["Maria", "Kumar", "Max"]
ages = [25, 31, 19] 
new_dict = {
    name:age
    for name, age in zip(names, ages)
}
print(new_dict)

print()

#Lambda with filter: use filter and lambda to keep only the products that cost more than 100
products = [["pen", 50], ["book", 300], ["bag", 1200]]
print(list(filter(lambda product: product[1] > 100, products)))

#as a list comprehension
products = [["pen", 50], ["book", 300], ["bag", 1200]]
new_list = [
    product
    for product in products
    if product[1] > 100
]
print(new_list)

#or
new_list = [
    [name, price]
    for name, price in products
    if price > 100
]
print(new_list)

#challenge: averages from a dictionary of lists: make a dictionary of each student's average mark
marks = {"Maria": [80, 90], "kumar": [70, 60]}
average = {
    k:sum(nums)/len(nums)
    for k, nums in marks.items() 
}
print(average)