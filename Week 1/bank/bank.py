greeting = input("Hey").strip().lower()
if greeting.startswith("hello"):
    print("$0")
if greeting.startswith("h"):
    print("$20")
else:
    print("$100")
