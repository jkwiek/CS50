import random
while True:
    try:
        level = int(input("Level: "))
        goal = random.randint(1,level)
        if level <=0:
            continue
    except ValueError:
        continue
    else:
        break

while True:
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



