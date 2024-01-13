import sys
import csv

if len(sys.argv) == 3:
    input, output = sys.argv[1], sys.argv[2]
    try:
        with open(input) as file:
            reader = csv.reader(file)
            next(reader)
            students = []
            for line in reader:
                name, house = line
                name = name.strip('\"')
                last, first = name.split(",")
                students.append(first, last, house)

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")
    finally:
        with open(output, "w") as file:
            write = csv.writer(file)
            write.writerows(students)



elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

