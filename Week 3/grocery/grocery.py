groceries={}
while True:
    try:
        item = input().upper()
    except EOFError:
        break
    else:
        if item in groceries:
            groceries[item]+=1
        else:
            groceries[item]=1
groceriesList = sorted(groceries)
for item in groceriesList:
    print(groceries[item], item)

