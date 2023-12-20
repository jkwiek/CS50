import random
while True:
    try:
        level = int(input("Level: "))
    except ValueError or level<=0:
        continue
while True:
    try:
        goal = random.randint(1,level)
        guess = int(input("Guess: "))
        if not 1<=guess<=level:
                continue
        elif guess < goal:
                print("Too small!")
                continue
        elif guess > goal:
                print("Too large!")
                continue
        else:
                break
    except ValueError:
            continue

print("Just right!")

