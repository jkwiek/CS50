plate = input("Plate: ")
for c in plate:
        if c.isdigit():
            print(plate.rsplit(sep=c,maxsplit=1)[0])

#if plate.partition(c)[1].isalpha() and not plate.rpartition(c)[2].startswith("0"):
# split at number c: after the number must be only numbers 
