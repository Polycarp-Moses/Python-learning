#Search

#startswith()
phone = "+254-705-097-054" #check if number is kenyan
print(phone.startswith("+254"))
print(phone.startswith("+255"))

#endswith()
email = "mosekamau007@gmail.com" #check whether email is gmail
print(email.endswith("gmail.com"))

file ="data_backup.csv" #is the file a csv? check the extension (.csv)
file.endswith(".csv")

#in operator
#check whether the user gives a valid email address
email = "mosekamau007@gmail.com" #is the email valid? check for @
print("@" in email)

#check if the URL is an API endpoint
url = "https://api.company.com/vi/data"
print("/api" in url)

#find()

phone1 = "+254-705-097-054"
phone2 = "254-719-804-375"
phone3 = "0054-719-804-375"
phone4 = "0018-222-345-522"
phone5 = "0333-843-993-882"

print(phone1.find("-")) #returns the starting position

#find() is great when combined with other methods to add dynamics
  #EXAMPLE: extract only phone number without country code

print(phone1[5:]) #slicing
print(phone2[4:]) #slicing
#Hardcoding the start position like above doesn's work when the country code length changes
#Do this instead

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
print(phone4[phone4.find("-")+1:])
print(phone5[phone5.find("-")+1:])