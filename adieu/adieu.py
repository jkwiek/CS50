import inflect
p = inflect.engine()
Names=[]

while True:
    try:
        Name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        Names.append(Name)

Names = p.join(Names)
print("Adieu, adieu, to", Names)




