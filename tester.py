plate = input("Plate: ")
for c in plate:
        if c.isdigit():
            print(plate.split(sep=c,maxsplit=1)[1])

#if plate.partition(c)[1].isalpha() and not plate.rpartition(c)[2].startswith("0"):