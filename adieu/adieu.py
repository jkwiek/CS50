Names=[]
while True:
        try:
            Name = input("Name: ")
            continue
        except EOFError:
            break
        else:
            Names =+ Name
Names= p.join(Names)
print("Adieu, adieu, to", Names)




