input = input("Input: ")
print("Output: ", end="")

for character in input:
    match character:
        case "a" | "e" | "i" | "o" | "u":
            print("", end= "", sep="")
        case _:
            print(character, sep="", end="")
print("\n")

