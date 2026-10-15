#Wjy do we need Else in loop?
# Search and validate data

# Task: Check for missing names in a list
names = ["Moses", "Mercy", None, "Imani"]
for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")
print()

#Task: Check if all files are csv files
files = ["data1.csv","report.pdf", "report.txt", "report2.csv"]
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not a csv")
        break
else:
    print("All files are csv")
