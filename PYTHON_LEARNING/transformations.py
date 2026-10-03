#Transformations
price = "1234,56" # replace the comma with a dot
price.replace(",", ".") #syntax for replacing old value with new
print(price.replace(",", ".")) #print new value

phone = "0705-097-054" #replace - with /
print(phone.replace("-", "/"))
print()

phone = "0705-097-054" #remove -
print(phone.replace("-", ""))

price = "$2,347.73"
print(price.replace("$", "") .replace(",", "")) #remove $ sign then remove comma