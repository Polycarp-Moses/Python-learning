#Break vs Continue: Real world applications
#Task: Loop through a list of days and print only the working days, skipping the weekends

days = ['Monday', 'Sunday', 'Wednesday', 'Tuesday', 'Thursday', 'Saturday']
weekends = ['Saturday', 'Sunday']
for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")

print()

#Task: Scan emails to block unsafe data from entering your system

emails = ['data@gmail.com', 'moses@outlook.de', 'DROP TABLE USERS; kamau@gmail.com']
for email in emails:
    if ';' in email:
        print("SQL Injection: Hacker Attack")
        break
    print(f"Processing Email: {email}")
