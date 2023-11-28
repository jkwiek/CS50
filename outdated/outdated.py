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
            month, day, year = input("Date: ").replace(",","").replace("-"," ").split(" ")
            month= monthvalid(month)
            day= dayvalid(day)
            year= yearvalid(year)
            if not (monthvalid(month) and dayvalid(day) and yearvalid(year)):
                continue
        except ValueError:
            continue
        else:
            print(year, month, day, sep="-")
            break

def monthvalid(month):
    if month in months:
        month = int(months.index(month)) + 1
        month = str(month).zfill(2)
        return month
    elif 1 <= int(month) <= 12:
        month = month.zfill(2)
        return month
    else:
        return False
def dayvalid(day):
    if 1<= int(day) <= 31:
        day = day.zfill(2)
        return day
    else:
        return False
def yearvalid(year):
    if len(year)==4:
        return year
    else:
        return False

main()
