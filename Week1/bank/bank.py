greeting = input("Greeting: ").strip().lower()
if greeting.startswith("hello") == True:
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
