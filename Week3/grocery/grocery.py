groceries={}
def main():
    getinputs()
    sortprint(groceries)
    
def getinputs():
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

def sortprint(groceries):
    groceriesList = sorted(groceries)
    for item in groceriesList:
        print(groceries[item], item)

main()




