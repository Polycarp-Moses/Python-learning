#and has higher priority than or. not has the highest priority
#use parenthesis () to control order

# Allow access only if the user is logged in or they are guest but they must not be banned

is_logged_in = True
is_guest = False
is_banned = False

print(is_logged_in or is_guest and not is_banned)

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned) #use parenthesis