import sys
def main():
    if len(sys.argv) == 2:
        request = sys.argv[1]
        if request.split(".")[1] != "py":
                sys.exit("Not a Python file")
        try:
            file = open(request)
            lines = []
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
                #figure out a way to make the file be found not just within the folder but generally
            with open(request) as file:
                for line in file:
                    if not line.lstrip().startswith("#") and not line.strip()=="":
                        lines.append(line)
            print(len(lines))

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
