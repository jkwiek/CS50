input = input("Input: ")
print("Output: ", end="")

for character in input:
    if character == "a","e","i","o","u":
        print("", end="", sep="")
    else:
        print(character, end="", sep="")
