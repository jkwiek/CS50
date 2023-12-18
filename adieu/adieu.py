import inflect
p = inflect.engine()
Names=[]
while True:
        try:
            Name = input("Name: ")
        except EOFError:
            break
        else:
            Names.append(Name)
Names= p.join(Name)
print("Adieu, adieu, to", Names)




