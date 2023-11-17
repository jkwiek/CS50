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
    lengthvalid(plate) and beginningvalid(plate) and numbersvalid(plate) and charactersvalid(plate)

def lengthvalid(plate):
    2 <= len(plate) <= 6

def beginningvalid(plate):
    plate[:2].isalpha()

def numbersvalid(plate):
    for c in plate:
        if c.isdigit():
            numbers = late.split((sep=c,maxsplit=1)[1]).is
            
            plate.split((sep=c,maxsplit=1)[1]).isdigit()
            plate.

def charactersvalid(plate):
    plate.find(".", " ", ",", "!", "?") == "-1"

main()
