import random

def valid_level(level):
    try:
        level = int(level)
    except ValueError:
        return False
    else:
        if level <= 0:
            return False
        else:
            return True
def correct_guess(guess):
    try:
        guess = int(guess)
    except ValueError:
        return False
    else:
        if not 1<=int(guess)<=int(level):
            return False
        elif guess < goal:
            print("Too small!")
            return False
        elif guess > goal:
            print("Too large!")
            return False
        else:
            return True

level = input("Level: ")
while valid_level(level) == False:
    level = input("Level: ")

goal = random.randint(1,int(level))

guess = input("Guess: ")
while correct_guess(guess) == False:
    guess = input("Guess: ")

print("Just right!")



