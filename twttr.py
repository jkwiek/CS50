input = input("Input: ")
print("Output: ", end="")
vowels = ["a","e","i","o","u"]
for character in input:
    if character not in vowels:
        print(character, end= "")
