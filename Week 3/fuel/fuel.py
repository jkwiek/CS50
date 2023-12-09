while True:
    try:
        x,y = input("Fraction: ").split("/")
        result = int(x) / int(y) * 100
    except(ValueError, ZeroDivisionError):
        continue
    if result <0 or result >100:
        continue
    else:
        break

if result <= 1:
    print("E")

elif result >=99:
    print("F")

else:
    result = round(result)
    print(result, "%", sep="")

