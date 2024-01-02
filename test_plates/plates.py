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
    elif not s.isalnum():
        return False
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            numbers = s.split(sep = c)[1]
            if not numbers.isdigit():
                return False
    else:
        return True

if __name__ == "__main__":
    main()


