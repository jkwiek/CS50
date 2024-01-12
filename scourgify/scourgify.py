import sys


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
            

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

#create dict students
#rewrite
