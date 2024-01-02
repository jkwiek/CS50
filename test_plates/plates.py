def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    elif not s[:2].isalpha():
        return False
    elif for c in s:
        if c.isdigit():
            numbers = s.split(sep = c,maxsplit=1)[1]
            if not numbers.isdigit() and c == "0":
                return False
        elif not plate.isalpha():
            return False
    elif not plate.isalnum():
        return False
    else:
        return True

if __name__ == "__main__":
    main()


