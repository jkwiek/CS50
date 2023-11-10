def main():
    convert()
    if 7.00 <= value <= 8.00 == True:
        print ("breakfast time")
    elif 12.00 <= value <= 13.00:
        print ("lunch time")
    elif 18.00 <= value <= 19.00:
        print ("dinner time")

def convert():
    hour, minute = time.split(':')
    if input("time: ").endswith("p.m."):
        hour, minute = time.split(':').removesuffix("p.m.")
        hour = int(hour)+12
    else:
        hour, minute = time.split(':').rstrip("a.m.")
        hour = int(hour)

    value = hour + minute/60
    return(value)

if __name__ == "__main__":
    main()

