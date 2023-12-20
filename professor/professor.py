import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError
            else:
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    integer = random.getrandbits(level)
    print(integer)

def main():
    get_level()
    generate_integer(level)


if __name__ == "__main__":
    main()
