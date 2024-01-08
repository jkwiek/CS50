import sys


if len(sys.argv) == 3:
    input, output = sys.argv[0], sys.argv[1]
    if not input.endswith(".csv") and not output.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(input) as file:
            students = []
            for line in file:
                last, first =  line["name"].split(",")
                print(first, last)
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
