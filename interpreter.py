x, y, z = input("expression: ").split(" ")
x = x.int()
z = z.int()
if y == "+":
    print(f"{(x+z):.1f}")
elif y == "-":
    print(x-z)
elif y == "/":
    print(x/z)
elif y == "*":
    print(x*z)

