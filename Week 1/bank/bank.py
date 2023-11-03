greeting = input("Greeting: ").strip().lower()
if greeting.startswith("hello"):
    print("$0")
if greeting.startswith("hello") and greeting.startswith("h"):
    print("$20")
else:
    print("$100")
