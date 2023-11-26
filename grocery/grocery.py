while True:
    try:
        food = input()
    except EOFError:
        break
    else:
        amount = list.count(food)
        list ={}
        list[amount]=food
        print(list)

#capitalize, number, alphabetize, print
