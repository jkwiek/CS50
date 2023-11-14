variable = input("camelCase: ")
print("snake_case:", end=" ")

for character in variable:
    if character.isupper():
        print("_", character.lower(), sep="")
    else:
        print(character, end="")

