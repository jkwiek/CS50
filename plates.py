#“All vanity plates must start with at least two letters.” yes
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” yes
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”
def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if lengthvalid(plate) and beginningvalid(plate) and numbersvalid(plate) and charactersvalid(plate):
        return True
    else:
        print("FalseA")

def lengthvalid(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        print("FalseB")

def beginningvalid(plate):
    if plate[:2].isalpha():
        return True
    else:
        print("FalseC")


def numbersvalid(plate):
    for c in plate:
        if c.isdigit():
            numbers = plate.split(sep = c,maxsplit=1)[1]
            if numbers.isdigit() and c != "0":
                return True
            else:
                print("FalseD")

def charactersvalid(plate):
    characters=[".", " ", ",", "!", "?"]
    for char in characters:
        if char not in plate:
            return True
        else:
            print("FalseE")

main()
