import random
n = int(input("Level: "))
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

