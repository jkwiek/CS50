while True:
    try:
        x,y = input("Fraction: ").split("/")
        result = int(x) / int(y) * 100
    except:
        continue
    else:
        break
result = round(result)
print(result, "%", sep="")

