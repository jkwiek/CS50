groceries={}
while True:
    try:
        food = input()
    except EOFError:
        break
    else:
        amount = groceries.count(food)
        groceries[amount]=food
        print(groceries)

#capitalize, number, alphabetize, print
