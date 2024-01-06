import sys
from tabulate import tabulate

if len(sys.argv) == 2:
    request = sys.argv[1]
    if not request.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(request) as file:
            table = []
            print(tabulate(file,headers="firstrow",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")



