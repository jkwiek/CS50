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
            month = None
            day = None
            year = None
            if "/" in date:
                nummonth, day, year = date.split("/")
                month = convert_nummonth(nummonth)
            elif "," in date:
                alphamonth, day, year = date.replace(",","").split(" ")
                month = convert_alphamonth(alphamonth)
            if None in (month, convert_day(day), convert_year(year)):
                    continue

        except (ValueError):
            continue
        else:
            print(convert_year(year), month, convert_day(day), sep="-")
            break

def convert_alphamonth(alphamonth):
    if alphamonth in months:
        alphamonth = int(months.index(alphamonth)) + 1
        alphamonth = str(alphamonth).zfill(2)
        return alphamonth
    else:
        return None
def convert_nummonth(nummonth):
    if 1 <= int(nummonth) <= 12:
        nummonth = nummonth.zfill(2)
        return nummonth
    else:
        return None
def convert_day(day):
    if 1<= int(day) <= 31:
        day = day.zfill(2)
        return day
    else:
        return None
def convert_year(year):
    if len(year)==4:
        return year
    else:
        return None

main()
