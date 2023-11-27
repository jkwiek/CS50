#groceries[key]=value
groceries={}
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        if item in groceries:
            groceries[item]+=1
        else:
            groceries[item]=1
groceriesList = sorted(groceries)
for item in groceriesList:
    item_upper = item.upper()
    print(groceries[item], item_upper)

#capitalize, number, alphabetize, print
