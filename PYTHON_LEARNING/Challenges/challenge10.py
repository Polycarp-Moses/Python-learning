#Check whether any filename appears more than once

files = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']
for file in files:
    if files.count(file) >1:
        print(f"Duplicate found: {file}")
        break 
else: 
    print("All files are unique")