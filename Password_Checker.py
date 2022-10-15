def chkpass(pword):
    passShort = False
    passLong = False
    passUpper = False
    passLower = False
    passNumber = False
    passSymb = False
    passChar = '\!@#$%^&*()_+/'

    for char in pword:
        if not passUpper and char.upper():
            passUpper = True

    if len(pword) <= 16:
        passShort = True

    if len(pword) >= 8:
        passLong = True

    for char in pword:
        if char.isupper():
            passUpper = True

    for char in pword:
        if char.islower():
            passLower = True

    for char in pword:
        if char.isdigit():
            passNumber = True

    for char in pword:
        if char in passChar:
            passSymb = True

    if passShort and passLong and passUpper and passLower and passNumber and passSymb:

        return True

    else:
        return False

password = input('Enter your password')

if chkpass(password):
    print('all good')

else:
    print('Not valid')









