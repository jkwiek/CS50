groceries={}
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        if item in groceries:
            groceries[amount]=+1
print(groceries)

#capitalize, number, alphabetize, print
