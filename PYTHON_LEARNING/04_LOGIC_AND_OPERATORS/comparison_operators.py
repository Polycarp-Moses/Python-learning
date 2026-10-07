#Comparison operators-compares two values and retun True or False based on the result
# == equal to
# != not eqaual
# < less than
# <= less than or equal
# > greater than
# >= greater than or equal

print(10==10)
print(10 != 10)
print(7 > 3)
print(7 >= 3)
print(3 < 7)
print ( 3<= 7)

#strings can be compared too
print("a" < "b")
print("a" == "b")
print("a" == "A") #python is case sensitive so these are not the same

#chained comparion: check multiple conditions in one line, just like math 
print(1 < 4 > 6) #evaluates from left to right, checking each condition one by one