import sys

if len(sys.argv) == 2:
    request = sys.argv[1]
    if request.split(".")[1] != "py":
        sys.exit("Not a Python file")
    try:
        total_lines = 0
        with open(request) as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.strip()=="":
                    lines+=1
            print(total_lines)
        except FileNotFoundError:
            sys.exit("File does not exist")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


