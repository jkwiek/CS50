def main():
    greeting = input("Greeting: ").strip()
    money = value(greeting)
    print(f"${money}")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

