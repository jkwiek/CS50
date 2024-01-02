def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(plate) <= 6:
        return False
    elif not plate[:2].isalpha():
        return False
    elif for c in plate:
        if c.isdigit():
            numbers = plate.split(sep = c,maxsplit=1)[1]
            if not numbers.isdigit() and c == "0":
                return False
        if not plate.isalpha():
            return False
    elif not plate.isalnum():
        return False
    else:
        return True

if __name__ == "__main__":
    main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if lengthvalid(plate) and beginningvalid(plate) and numbersvalid(plate) and charactersvalid(plate):
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
main()
