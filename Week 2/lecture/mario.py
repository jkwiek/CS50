def main():
    printcolumn(3)
    printrow(4)

def printcolumn(height):
    print("#\n" * height, end="")

def printrow(row):
    print("?" * row)

def printsquare(size):
    for i in range(size):
            print("#" * size)


main()

