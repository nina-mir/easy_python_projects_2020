# code to slice a valid email address
# into its username and domain name
# currently this code only checks for @ existence
# as a check for validity of the email address -- Jan 13, 2020

email = input("Enter a valid email address: ")
premise = True


def validate_at(email):
    flag = True
    try:
        atIndex = email.index('@')
        if (atIndex == 0):
            print('Error @1')
            return False
    except ValueError:
        print('Error @2')
        return False
    return flag


def validate(email):
    x = 0
    if not email.isprintable():
        x += 1
        print('Error 12 x = ', x)
    if (len(email) == 0):
        x += 1
        print('Error 15 x = ', x)
    if not validate_at(email):
        x += 1
    return x


while premise:
    x = validate(email)

    if x > 0:
        email = input("Enter a valid email address: ")
    elif x == 0:
        name = email.split("@", 1)
        #print(name)
        if validate_at(name[0]) | validate_at(name[1]):
            email = input("Enter a valid email address: ")
        elif (len(name[0]) == 0) | (len(name[1]) == 0):
            email = input("Enter a valid email address: ")
        else:
            print('Valid Email address detected! Yay!')
            print(name)
            premise = False
