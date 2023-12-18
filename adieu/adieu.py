import inflect
p = inflect.engine()
Names=[]

while True:
    try:
        Names.append(Name)
    except EOFError:
        break

Names = p.join(Names)
print("Adieu, adieu, to", Names)




