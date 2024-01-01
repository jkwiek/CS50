def main():
    input = input("Input: ")
    input = shorten(input)
    print(f"Output: {input}")

def shorten(word):
    vowels = ["a","e","i","o","u"]
    for char in word:
        if char in vowels:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()


