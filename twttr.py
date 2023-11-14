input = input("Input: ")
print("Output: ", end="")

for character in input:
    if character == "a" or "e" or "i" or "o" or "u":
        print("", end="")
    else:
        print(character, end="")
