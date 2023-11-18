plate = input("Plate: ")
for c in plate:
    if c.isdigit():
        numbers = plate.split(sep = c,maxsplit=1)[1]
        if numbers.isdigit() and c != "0":
            print("True")
        else:
            print("False")



#if plate.partition(c)[1].isalpha() and not plate.rpartition(c)[2].startswith("0"):
#split at number c: after the number must be only numbers, before must be only letters
