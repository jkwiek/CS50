import random


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



