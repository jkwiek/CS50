import sys
import csv

if len(sys.argv) == 3:
    input, output = sys.argv[1], sys.argv[2]
    try:
        with open(input) as file:
            reader = csv.DictReader(file, fieldnames= ["name", "house"])
            for line in reader:
                name = line["name"]
                house = line["house"]
                name = name.strip('\"')
                last, first = name.split(",")
                with open(output, "w") as file:
                    write = csv.writer(file)
                    write.writerow([first, last, house])

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

