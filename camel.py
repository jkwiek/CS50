variablename = input("camelCase: ")
print("snake_case: ", end="")
for char in variablename:
    if char.isupper():
        print("_", char.lower(), end="", sep="")
    else:
        print(char, end="")
print()

