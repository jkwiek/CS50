def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            percentage = int(x) / int(y) * 100
        except (ValueError, ZeroDivisionError):
            continue
        if percentage <0 or percentage >100:
            continue
        else:
            return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >=99:
        return "F"

    else:
        percentage = round(percentage)
        return f"{percentage}%"

if __name__ == "__main__":
    main()
