# Logical Operations

#and/or Operators
#and = True if both conditions are true
#or = True if at least one is true

print(3 > 1 and  5<1)
print(3 > 1 and  5>1)

print(3 > 1 or  5<1)
print(3 < 1 or  5<1)

#Code to check if computer system is under pressure

cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

#check user credentials before login

email = True
password = False
print(email and password)

#Not Operator
#Not = Reserses True <-> False
print(not 3>2)
print(not True)
print(not False)

name = "" #the boolean of empty is False
print(name)
print(not name)
print(not 0) # zero if False so will be flipped to True