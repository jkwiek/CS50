def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()

input = input("Input: ")
vowels = ["a","e","i","o","u"]
print("Output: ", end="")
for char in input:
    if char not in vowels:
        print(char, end="")
print()
