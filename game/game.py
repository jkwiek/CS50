import random
while True:
    try:
        n = int(input("Level: "))
        goal = random.randint(1,n)
        guess = int(input("Guess: "))
        
        if n <=0:
            continue
        if not 1<=guess<=n:
            continue
        elif guess < goal:
            print("Too small!")
        elif guess > goal:
            print("Too large!")
        else:
            break

print("Just right!")

