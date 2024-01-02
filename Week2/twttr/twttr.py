input = input("Input: ")
vowels = ["a","e","i","o","u"]
for char in input:
    if char.lower() in vowels:
        input = input.replace(char, "")
print(f"Output: {input}")

