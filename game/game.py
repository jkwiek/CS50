import random

def valid_level(level):
    try:
        level = int(level)
    except ValueError:
        return False
    else:
        if level <= 0:
            return False
def correct_guess(guess):
    try:
        guess = int(guess)
    except ValueError:
        return False
    else:
        if 1<=guess<=level:
            return False
        elif guess < goal:
            print("Too small!")
            return False
        elif guess > goal:
            print("Too large!")
            return False

level = input("Level: ")
while not valid_level(level):
    level = input("Level: ")

goal = random.randint(1,level)

guess = input("Guess: ")
while not correct_guess(guess):
    guess = input("Guess: ")

print("Just right!")



