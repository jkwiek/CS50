import random

def valid_level(level):
    try:
        level = int(level)
    except ValueError:
        return False
    else:
        if level <= 0:
            return False
def valid_goal(goal):
    try:
        guess = int(level)
    except ValueError:
        return False
    

level = input("Level: ")
    while not valid_level(level):
        level = input("Level: ")

goal = random.randint(1,level)

while guess = None:
    guess = input("Guess: ")
    validate(guess)
    if 1<=guess<=level:
        break
        elif guess < goal:
            print("Too small!")
        elif guess > goal:
            print("Too large!")
        else:
            break
    except ValueError:
        continue

print("Just right!")



