import sys
import csv

if len(sys.argv) == 3:
    input, output = sys.argv[1], sys.argv[2]
    try:
        with open(input) as file:
            students = []
            for line in file:
                name, house = line.split(",")
                last, first = name.split(",")
                student = {"first":first, "last":last, "house":house}
                students.append(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")
    finally:
        with open(output, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "home"])
            writer.writerow({"first": first, "last": last, "house": house})

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

