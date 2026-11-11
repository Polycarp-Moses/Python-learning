# MIXED ARGUMENTS
# You can mix positional and keyword arguments
# You must start with the positional arguments before keyword arguments - you CANNOT start with the keyword argument

def clean_name(first_name, last_name, country):
    first = first_name.strip().lower().capitalize()
    last = last_name.strip().lower().capitalize()
    full_name = first + " " + last
    print(full_name, "From", country)
clean_name(" MariA  ", last_name= "SMITH", country= "DE") #mixed argument
clean_name("KAMAU", last_name= "MOSES", country= "KE") #mixed

#Tip: mixed arguments not recommended