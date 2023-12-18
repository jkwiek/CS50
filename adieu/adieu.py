import inflect
p = inflect.engine()
Names=[]
while True:
        try:
            Name = input("Name: ")
        except EOFError:
            break
        else:
            Names = Names.append(Name)
Names = p.join(Names)
print("Adieu, adieu, to", Names)




