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
        month, day, year = input().strip(",").partition(" ", "/", ",")
        if month in months:
            month = int(months.index(month)) + 1
        if 1 <= month.int() <= 12:
            if len(month)  == 1:
                month = 0 + month

        if 1<= int(day) <= 31:
            if len(day)  == 1:
                day = 0 + day

        if len(year.int())==4:
            year = year
        else:
            continue
    except ValueError:
        continue
    else:
        print(year, month, day, sep="-")
