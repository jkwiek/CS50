def main():
    convert()
    if 7.00 <= time <= 8.00 == True:
        print ("breakfast time")
    elif 12.00 <= time <= 13.00:
        print ("lunch time")
    elif 18.00 <= time <= 19.00:
        print ("dinner time")

def convert():
    time = input("time: ").find(" ")
    if input("time: ").find(" p.m.")
        hour, minute = time.split(':').removesuffix("p.m.")
        if hour = int(hour)= 12
        hour = int(hour)+12
        return(hour and minute)
    else:
        hour, minute = time.split(':').rstrip("a.m.")
        hour = int(hour)
        return(hour and minute)
     return(hour + minute/60)

if __name__ == "__main__":
    main()

