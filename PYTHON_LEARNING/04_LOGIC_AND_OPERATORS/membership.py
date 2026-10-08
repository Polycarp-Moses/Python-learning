#Membership (in) Operator - checks if a value is inside another value, like a string, list, tuple, or other sequence

print("o" in "python")
print("f" not in "python")
print(3 in [1,2,3])

#secturity check: Validate that the domain is not on the banned list
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)