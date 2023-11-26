groceries={}
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        if item in groceries:
            groceries[key]+=1
        else:
            groceries["1"]=item
print(groceries)

#capitalize, number, alphabetize, print
