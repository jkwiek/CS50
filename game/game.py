import random

def validate(input):


try:
    level = int(input("Level: "))
    if level <=0:
        continue
    except ValueError:
        continue
    else:
        goal = random.randint(1,level)

    try:
        guess = int(input("Guess: "))
        if not 1<=guess<=level:
            continue
        elif guess < goal:
            print("Too small!")
        elif guess > goal:
            print("Too large!")
        else:
            break
    except ValueError:
        continue

print("Just right!")



