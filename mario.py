def main():
    printcolumn(3)
    printrow(4)

def printcolumn(height):
    print("#\n" * height, end="")

def printrow(row):
    print("?" * row)

main()

