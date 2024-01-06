import sys

if len(sys.argv) == 2:
    request = sys.argv[1]
    if request.split(".")[1] != "csv":
        sys.exit("Not a Python file")
    try:
        with open(input) as file:
            print(tabulate(file, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")



