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

groceries= groceries.key_value.iterkeys()
print(groceries)

#capitalize, number, alphabetize, print
