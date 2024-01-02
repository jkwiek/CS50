def main():
    greeting = input("Greeting: ").strip().lower()
    value = value(greeting)
    print(f"${value}")

def value(greeting):
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

