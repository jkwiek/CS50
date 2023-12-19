import random
while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    else:
        break
    
goal = random.randint(1,n)
while True:
    try:
        guess = int(input("Guess: "))
        if not 1<=guess<=n:
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

