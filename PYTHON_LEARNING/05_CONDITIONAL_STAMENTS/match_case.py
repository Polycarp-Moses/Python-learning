#Match case
#Evaluate a value against multiple values
#Runs the code of the first match

#Use case task: convert the full country names into 2-letter abbreviations

country = "India"
match country:
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case "China":
        print("CH")
    case "Kenya":
        print("KE")
    case "United States" | "USA": #Add a pipe to check mutliple values in a single case
        print("US")
    case _:
        print("Unkown Country")