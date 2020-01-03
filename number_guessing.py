# guessing a number between 1 to 100
import random

target = int(random.randrange(0,100,1))
print("You have 5 tries to guess what number between 0 and 100 this program has chosen randomly!")

def is_it_correct(guess):
    distance = guess - target
    if distance > 0:
        print("Guess a smaller number next time!")
        return False
    elif distance < 0:
        print("Guess a larger number next time!")
        return False
    else:
        print("Perfect! Yay!")
        return True

def try_guessing():
    while True:
       inp = int(input("Enter an integer number: "))
       if is_it_correct(inp):
           return

try_guessing()
