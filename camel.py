variablename = input("camelCase: ")
print("snake_case: ")
for char in variablename:
    if char.isupper():
        print("_", char.lower(), end="")
    else:
        print(char, end="")
