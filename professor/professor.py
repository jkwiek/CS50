import random

def main():
    level = get_level()
    for problems <= 10:
        number= generate_integers(level)
        solution = number + generate_integers(level)


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

def generate_integers(level):
    integer= []
    for n<=2
        for _ in range(level):
            digit = str(random.randint(0,9))
            integer += [digit]
    integer = "".join(integer)


if __name__ == "__main__":
    main()
