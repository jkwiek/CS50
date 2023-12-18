import inflect
p = inflect.engine()
Names=[]
while True:
        try:
            Name = input("Name: ")
            Names.append(Name)
        except EOFError:
            break
        else:
            Names= p.join(Name)
print("Adieu, adieu, to", Names)




