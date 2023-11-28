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
        month, day, year = input().split(" ", "/")
        if month in months:
            month = int(months.index(month)) + 1
        if 1 <= month.int() <= 12:
            if len(month)  == 1:
                month = month + 1
            else:
                month = month
        if 1<= int(day) <= 31:
            if length(day)  == 1:
                day= f{day: 02f}
            else:
                day = day
        if length(year.int())==4:
            year = year
        else:
            continue
    except ValueError:
        continue
    else:
        print(year, month, day, sep="-")
