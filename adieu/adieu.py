Names=[]
while True:
        try:
            Name = input("Name: ")
        except EOFError:
            break
        else:
            Names = Name.append()
print("Adieu, adieu, to", Names)




