# code to slice a valid email address
# into its username and domain name

email = input("Enter a valid email address: ")
premise = True
count = 0

while premise:
    x = validate(email)

    if x > 0:
        email = input("Enter a valid email address: ")
    elif x == 0:
        print('23 x = ', x)
        name = email.split("@", 2)
        print(name)
        premise = False


def validate(email):
    x = 0
    if not email.isprintable():
        x += 1
        print('Error 12 x = ', x)
    if (len(email) == 0):
        x += 1
        print('Error 15 x = ', x)
    try:
        atIndex = email.index('@')
        if (atIndex == 0):
            print('invalid input! please try again.')
            x += 1
            print('19 x = ', x)
    except ValueError:
        print('invalid input! please try again.')
        x += 1
        print('Error 19-0 x = ', x)
    return x
