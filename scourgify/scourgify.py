import sys


if len(sys.argv) == 2:
    input, output = sys.argv[1][2]
    if not request.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(input) as file:

    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
