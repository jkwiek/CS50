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
groceries = sorted(groceries)
for item in groceries:
    item = item.upper()
    print(groceries[item], item)

#capitalize, number, alphabetize, print
