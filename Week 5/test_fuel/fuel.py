def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            percentage = int(x) / int(y) * 100
            percentage = int(round(percentage))
            if percentage <0 or percentage >100:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            
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
