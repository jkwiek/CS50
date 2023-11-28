months = [
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
month = input()
if month in months:
    month = int(months.index(month)) + 1
    month = str(month).zfill(2)
    print(month)
