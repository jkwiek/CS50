Names=[]
while True:
        try:
            Name = input("Name: ")
            continue
        except EOFError:
            break
        else:
            Names =+ Name
print("Adieu, adieu, to", p.join(Names))




