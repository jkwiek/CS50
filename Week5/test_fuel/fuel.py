def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break
    print(gauge(percentage))

def convert(fraction):
        x,y = fraction.split("/")
        percentage = int(x) / int(y) * 100
        percentage = int(round(percentage))
        if y=="0" :
            raise ZeroDivisionError
        if percentage <0 or percentage >100:
            raise ValueError
        else:
            return percentage

def gauge(percentage):
    if int(percentage) <= 1:
        return "E"

    elif int(percentage) >=99:
        return "F"

    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
