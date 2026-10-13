#Use case 1: for loop is used in the data world to move files or tables from one place to another
#Example:
#for filename in [file]:
    #df = pd.read_csv(src)
    #df.to_csv(tgt, index=False)

#Use case 2: can be used in data cleaning or data preparation

#Use case 3: you can combine for loop and the strip() function to iterate through or clean up columns
#Example:
#for col in df.columns:
    #df[col] = df[col].str.strip()

#We use for loops to go through values and aggregate data like summing, counting, or averaging
#Example: finding total of scores:

scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score #total = total + scores
    print("Current Total:", total)
print("Final Total:", total)

print()

#we use loops to transform data like cleaning data before processing
#Always clean your data first before manipulating or transforming it
files = ['Report.csv ', 'DATA.csv ', ' final.TXT '] #inconsistent casing and unnecessary spaces
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")

