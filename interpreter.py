x, y, z = input("expression: ").split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(f"{(x+z):.1f}")
elif y == "-":
    print(x-z)
elif y == "/":
    print(x/z)
elif y == "*":
    print(x*z)

