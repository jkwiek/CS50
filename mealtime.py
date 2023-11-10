def main():
    convert()
    if 7.00 <= value <= 8.00 == True:
        print ("breakfast time")
    elif 12.00 <= value <= 13.00:
        print ("lunch time")
    elif 18.00 <= value <= 19.00:
        print ("dinner time")

def convert():

    if input("time: ").endswith("p.m."):
        hour = int(hour)+12
    else
        hour = int(hour)
    hour, minute = time.split(':'):
    minute = int(minute)

    value = hour + minute/60
    return(value)

if __name__ == "__main__":
    main()

str.endswith(suffix[, start[, end]])
