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
while True:
    try:
        month, day, year = input().strip(",").replace("-"," ").split(" ")
        if month in months:
            alphaMonth = int(months.index(month)) + 1
        elif 1 <= int(month) <= 12:
            numMonth = month.zfill(2)
        if 1<= int(day) <= 31:
            day = day.zfill(2)
        if len(year)!= 4:
            continue
    except ValueError:
        continue
    else:
        print(year, month, day, sep="-")
