import sys
if len(sys.argv) == 2:
    request = sys.argv[1]
    try:
        file = open(request)
        lines = []
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        if file_name.split(".")[1] != "py":
            sys.exit("Not a Python file")
        else:
            #figure out a way to make the file be found not just within the folder but generally
            with open(request) as file:
                for line in file:
                    if not line.lstrip().startswith("#"):
                        lines.append(line)

            print(len(lines))

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

