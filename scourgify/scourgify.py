import sys
import csv

if len(sys.argv) == 3:
    input, output = sys.argv[1], sys.argv[2]
    try:
        with open(input) as file:
            reader = csv.DictReader(file, fieldnames= ["name", "house"])
            next(reader)
            for line in reader:
                house = line["house"]
                name = line["name"]
                name = name.strip('\"')
                last, first = name.split(",")
                with open(output, "a") as file:
                    write = csv.writer(file)
                    write.writerow([first, last, house])

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

