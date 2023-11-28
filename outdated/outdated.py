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
            month = int(months.index(month)) + 1
        elif 1 <= int(month) <= 12:
            if len(month)  == 1:
                month = 0 + month
        if 1<= int(day) <= 31:
            if len(day)  == 1:
                day = 0 + day
        len(year)==4
        else:
            continue
    except ValueError:
        continue
    else:
        print(year, month, day, sep="-")
