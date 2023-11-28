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
    elif 1 <= int(month) <= 12:
        month = month.zfill(2)
def dayvalid(day):
    if 1<= int(day) <= 31:
        day = day.zfill(2)
def yearvalid(year):
    len(year)==4

while True:
    try:
        month, day, year = input("Date: ").replace(",","").replace("-"," ").split(" ")
        if not monthvalid() or not dayvalid() or not yearvalid():
            continue
    except ValueError:
        continue
    else:
        print(year, month, day, sep="-")
