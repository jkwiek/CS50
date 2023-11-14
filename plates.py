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
    number = ["1","2","3","4","5","6","7","8","9"]
    if {
    plate[:2].isalpha(),
    2 <= len(plate) <= 6,
    for c in plate:
        if c.isdigit():
            if plate.partition(c)[2].isalpha():
                return True


    }:
        return(True)


main()
