def main():
    convert()
    if 7.00 <= time <= 8.00:
        print ("breakfast time")
    elif 12.00 <= time <= 13.00:
        print ("lunch time")
    elif 18.00 <= time <= 19.00:
        print ("dinner time")

def convert():
    hour, minute, x = input("time: ").split(":").split(" ")
    minute = int(minute)
    if x == "p.m.":
        hour = int(hour)+12
    else:
        hour = int(hour)
    time = hour+minute/60
    return time

main()
