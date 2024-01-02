def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if lengthvalid(s) and beginningvalid(s) and numbersvalid(s) and charactersvalid(s):
        return True

def lengthvalid(plate):
    if 2 <= len(plate) <= 6:
        return True

def beginningvalid(plate):
    if plate[:2].isalpha():
        return True

def numbersvalid(plate):
    for c in plate:
        if c.isdigit():
            numbers = plate.split(sep = c,maxsplit=1)[1]
            if numbers.isdigit() and c != "0":
                return True
        if plate.isalpha():
            return True
        
def charactersvalid(plate):
    if plate.isalnum():
        return True

if __name__ == "__main__":
    main()



