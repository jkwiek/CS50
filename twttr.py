input = input("Input: ")
for character in input:
    if character == "a" or "e" or "i" or "o" or "u":
        character = ""
    else:
        character = character
    print(character, end="")
