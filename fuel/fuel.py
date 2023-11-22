while True:
    try:
        x,y = input("Fraction: ").split("/")
        result = int(x) / int(y)
    except:
        continue
    else:
        print(result*100)
