import sys


if len(sys.argv) == 2:
    input, output = sys.argv[1][2]
    try:
        with open(request) as file:
            table = []
            for line in file:
                row = line.rstrip().split(",")
                table.append(row)
            print(tabulate(table,headers="firstrow",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
