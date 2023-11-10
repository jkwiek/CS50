def main():
    convert()
    if 7.00 <= x <= 8.00 == True:
        print ("breakfast time")
    elif 12.00 <= x <= 13.00:
        print ("lunch time")
    elif 18.00 <= x <= 19.00:
        print ("dinner time")

def convert():
    time = input("time: ")
    if " p.m." in time == True:
        hour, minute = time.split(':').removesuffix(" p.m.")
        if hour == "12":
            hour = int(12)
        else:
            hour = int(hour)+12
    else:
        hour, minute = time.split(':').removesuffix(" a.m.")
        hour = int(hour)

    x = hour + minute/60
    return(x)

if __name__ == "__main__":
    main()

