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
groceries = sorted(groceries).capitalize()
print(groceries,[groceries], sep=" ")

#capitalize, number, alphabetize, print
