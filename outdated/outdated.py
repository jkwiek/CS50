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
                alphamonth, day, year = date.split("/")
            elif "," in date:
                nummonth, day, year = date.replace(",","").split(" ")
            if None in (monthvalid(month), dayvalid(day), yearvalid(year)):
                continue
        except ValueError:
            continue
        else:
            print(yearvalid(year), monthvalid(month), dayvalid(day), sep="-")
            break

def monthvalid(alphamonth):
    if alphamonth in months:
        month = int(months.index(alphamonth)) + 1
        month = str(alphamonth).zfill(2)
        return month
    else:
        return None
def monthvalid(nummonth):
    if 1 <= int(nummonth) <= 12:
        month = nummonth.zfill(2)
        return month
    else:
        return None
def dayvalid(day):
    if 1<= int(day) <= 31:
        day = day.zfill(2)
        return day
    else:
        return None
def yearvalid(year):
    if len(year)==4:
        return year
    else:
        return None

main()
