def main():
    convert()
    if 7.00 <= x <= 8.00 == True:
        print ("breakfast time")
    elif 12.00 <= x <= 13.00:
        print ("lunch time")
    elif 18.00 <= x <= 19.00:
        print ("dinner time")

def convert():
    hour,minute = input("time: ").split(':')
    x = int(hour) + int(minute)/60
    return(x)

if __name__ == "__main__":
    main()

