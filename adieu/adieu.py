Names=[]
while True:
        try:
            Name = input("Name: ")
            Names = append(Name)
        except EOFError:
            break
        else:
            NamesList = p.join(Name)
print("Adieu, adieu, to", NamesList)




