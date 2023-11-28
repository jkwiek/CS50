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
def monthvalid(month):
    if month in months:
        month = int(months.index(month)) + 1
        month = str(month).zfill(2)
        return True
    elif 1 <= int(month) <= 12:
        month = month.zfill(2)
        return True
def dayvalid(day):
    if 1<= int(day) <= 31:
        day = day.zfill(2)
        return True
def yearvalid(year):
    len(year)==4
    return True

while True:
    try:
        month, day, year = input("Date: ").replace(",","").replace("-"," ").split(" ")
        if not monthvalid(month) or not dayvalid(day) or not yearvalid(year):
            continue
    except ValueError:
        continue
    else:
        print(year, month, day, sep="-")
