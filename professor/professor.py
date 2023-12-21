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
    number= []
    for _ in range(level):
        digit = str(random.randint(0,9))
        number += [digit]
    number = "".join(number)

if __name__ == "__main__":
    main()
