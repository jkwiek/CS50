import random
def main():
    level = input("Level: ")
    while valid_level(level) == False:
        level = input("Level: ")

    goal = random.randint(1,int(level))

    guess = input("Guess: ")
    while correct_guess(guess,goal,level) == False:
        guess = input("Guess: ")

    print("Just right!")

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
def correct_guess(guess,goal,level_int):
    try:
        guess = int(guess)
    except ValueError:
        return False
    else:
        if not int(1)<=guess<=level_int:
            return False
        elif guess < goal:
            print("Too small!")
            return False
        elif guess > goal:
            print("Too large!")
            return False
        else:
            return True
main()


