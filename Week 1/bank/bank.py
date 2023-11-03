greeting = input("Greeting: ").strip().lower()
if greeting.startswith("hello"):
    return True
else:
    return False
if True:
    print("$0")
if False and greeting.startswith("h"):
    print("$20")
else:
    print("$100")
