#“All vanity plates must start with at least two letters.” yes
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” yes
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if lengthvalid(plate)==True and beginningvalid(plate)==True and numbersvalid(plate)==True and charactersvalid(plate)==True:
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

def charactersvalid(plate):
    if plate.find(".", " ", ",", "!", "?") == "-1":
        return True

main()
