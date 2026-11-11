# DEFAULT PARAMETERS - parameter that has already a value, so if you don't pass anything, python uses that value automatically.

def clean_name(first_name, last_name, country = "n/a"):
    first = first_name.strip().lower().capitalize()
    last = last_name.strip().lower().capitalize()
    full_name = first + " " + last
    print(full_name, "From", country)

clean_name(" MariA  ", "SMITH", "DE") #positional

clean_name(first_name= "KAMAU", last_name= "MOSES", country= "KE") #keyword

clean_name("JOHN", "Smith") #default
