def main():
    time = input("time: ")
    convert(time)
    if 7.00 <= time <= 8.00:
        print ("breakfast time")
    elif 12.00 <= time <= 13.00:
        print ("lunch time")
    elif 18.00 <= time <= 19.00:
        print ("dinner time")

def convert(time):
    hour,minute = time.split(":")
    return (int(hour) + int(minute)/60)

if __name__ == "__main__":
    main()

