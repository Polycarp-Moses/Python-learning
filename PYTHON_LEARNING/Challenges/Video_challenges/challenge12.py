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