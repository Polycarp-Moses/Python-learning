#Check is the user is either an admin or moderator, and either they are not banned or they have verified their email 

user = "moderator"
is_banned = False
is_verified = True

print((user == "admin" or user == "moderator") and (not is_banned or is_verified))

