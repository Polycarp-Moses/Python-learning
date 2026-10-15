#Break statement
#It stops the loop immediately
#It jumps out and ends the loop right away

names = ['Moses', 'Mercy', '', 'Imani']
for name in names:
    if name == '':
        print("Empty value detected")
        break
    print(f"Name = {name}")

print()

#Continue Statement
#It skips one loop cycle without stopping the loop
#Skip this one and go next

names = ['Moses', 'Mercy', '', 'Imani']
for name in names:
    if name == '':
        print("Empty value detected")
        continue
    print(f"Name = {name}")

print()

#Pass Statement
#It is a placeholder where nothing happens
#For now just keep going..do nothing
#It is often used as a placeholder to be changed later
names = ['Moses', 'Mercy', '', 'Imani']
for name in names:
    if name == '':
        pass #todo: handle empty value
    print(f"Name = {name}")

print()

#Pass is often used as a placeholder to be changed later as shown below
names = ['Moses', 'Mercy', '', 'Imani']
for name in names:
    if name == '':
        name = name.replace('', 'unknown')
    print(f"Name = {name}")