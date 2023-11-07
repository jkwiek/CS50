def main():
    convert()
    if 7.00 <= time <= 8.00:
        print ("breakfast time")
    elif 12.00 <= time <= 13.00:
        print ("lunch time")
    elif 18.00 <= time <= 19.00:
        print ("dinner time")

def convert():
    time, part = input("time: ").split(' ')
    hour, minute = time.split(':')
    minute = int(minute)
    if part == "p.m.":
        hour = int(hour)+12
    else:
        hour = int(hour)
    time = hour + minute/60
    return(time)

main()
