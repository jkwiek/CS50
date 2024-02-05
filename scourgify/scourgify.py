import sys
import csv

if len(sys.argv) == 3:
    input, output = sys.argv[1], sys.argv[2]
    try:
        with open(input) as file:
            reader = csv.DictReader(file, fieldnames= ["name", "house"])
            next(reader)
            names = []
            for line in reader:
                house = line["house"]
                name = line["name"]
                name = name.strip('\"').replace(" ","")
                last, first = name.split(",")
                names.append({"first": first, "last": last, "house": house})
        with open(output, "w") as file:
            write = csv.DictWriter(file, fieldnames = ["first","last","house"])
            write.writeheader()
            for row in names:
                write.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
    
