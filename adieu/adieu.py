Names=[]
while True:
        try:
            Names = input("Name: ")
        except EOFError:
            break
        else:
            NamesList = p.join(Name)
print("Adieu, adieu, to", Names)




