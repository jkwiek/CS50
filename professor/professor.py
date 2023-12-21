import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError
            else:
                return(level)
        except ValueError:
            continue

def generate_integer(level):
    integer = None
    number= [integer]
    for _ in range(1,level+1):
        integer = random.randint(0,9)
        number += integer
        print(number)

if __name__ == "__main__":
    main()
