#username validator

username = "moses_kamau"

if username == "":
    print("Username cannot be empty")
elif not(len(username) >=4 and len(username) <= 15):
    print("Username must be between 4 and 15 characters")
elif not(username [0].isalpha()):
    print("Username must start with a letter")
elif not username.replace("_", "").isalnum():
    print("Must contain only letters, digits or underscores")
elif username in ["admin", "root", "user"]:
    print("Must not be one of admin, root, user")
else:
    print("Username is valid")
 