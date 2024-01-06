import sys
if len(sys.argv) == 2:
    request = sys.argv[1]
    try:
        file = open(request)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        if file.split(".")[1] =! "py":
            sys.exit("F)
elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

