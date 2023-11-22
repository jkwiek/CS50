while True:
    try:
        x,y = input("Fraction: ").split("/")
        result = int(x) / int(y)
    except:
        continue
    else:
        break
print(result*100, "%", sep="")
