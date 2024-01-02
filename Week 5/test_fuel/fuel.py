def main():
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            percentage = int(x) / int(y) * 100
            percentage = int(round(percentage))
            if percentage <0 or percentage >100:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            continue
        else:
            return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >=99:
        return "F"

    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
