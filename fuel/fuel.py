while True:
    try:
        x,y = input("Fraction: ").split("/")
        result = int(x) / int(y) * 100
    except:
        continue
    else:
        break
print(f"{result:1f}", "%", sep="")
