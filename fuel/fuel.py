while True:
    try:
        x,y = input("Fraction: ").split("/")
        result = int(x) / int(y) * 100
        if 0 <= result < 1:
                
        elif 99 <= result <= 100:
                print("F")
                break
        elif result <0 or result >100:
                continue
    except(ValueError, ZeroDivisionError):
        continue
    else:
        break
result = round(result)
print(result, "%", sep="")

