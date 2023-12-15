Names=[]
while True:
        try:
            Name = input("Name: ")
        except EOFError:
            break
        else:
            Names = Names.append(Name)
print("Adieu, adieu, to", Names)




