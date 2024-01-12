import sys
import csv

if len(sys.argv) == 3:
    input, output = sys.argv[1], sys.argv[2]
    try:
        with open(input) as file:
            students = []
            for line in file:
                name = line.d

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")
    finally:
        with open(output, "w") as file:
            write = csv.writer(file)

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

