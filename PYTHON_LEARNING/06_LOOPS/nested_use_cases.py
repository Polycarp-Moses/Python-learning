#Nested loops use cases
#1. Crossing(combining/pairing) data
#Example: Pairing colors and sizes in a product catalogue
colors = ["red", "blue", "green"]
sizes = ["L", "M", "S"]
for color in colors:
    for size in sizes:
        print(f"{color} - Size {size}")

print()

#2. Navigate hierarchy- or go through layers
#Example: creating multiple reports for each year, each month and each day
years = [2026, 2027]
months = ["Jan", "Feb"]
days = range(1, 29)

for year in years:
    for month in months:
        for day in days:
            print(f"report_{year}_{month}_{day}.csv")

print()

#Another example: Navigating through Tables and Columns
# SELECT count(*) FROM customers where id is NULL (counts the rows in the customers table where the id is empty)
tables = ["customers", "orders", "products", "prices"]
columns = ["id", "creation_date"]
for table in tables:
    for column in columns:
        print(f"SELECT count(*) FROM {table} WHERE {column} IS NULL;")
