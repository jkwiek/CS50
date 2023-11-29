months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                nummonth, day, year = date.split("/")
                month = convert(nummonth)
            elif "," in date:
                alphamonth, day, year = date.replace(",","").split(" ")
                month = convert(alphamonth)
            if None in (month, convert(day), convert(year)):
                continue
        except ValueError:
            continue
        else:
            print(convert(year), month, convert(day), sep="-")
            break

def convert(alphamonth):
    if alphamonth in months:
        alphamonth = int(months.index(alphamonth)) + 1
        alphamonth = str(alphamonth).zfill(2)
        return alphamonth
    else:
        return None
def convert(nummonth):
    if 1 <= int(nummonth) <= 12:
        nummonth = nummonth.zfill(2)
        return nummonth
    else:
        return None
def convert(day):
    if 1<= int(day) <= 31:
        day = day.zfill(2)
        return day
    else:
        return None
def convert(year):
    if len(year)==4:
        return year
    else:
        return None

main()
