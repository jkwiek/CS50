import random

def main():
    get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            break
        except ValueError:
            continue
    return level


def generate_integer(level):
    random.getint


if __name__ == "__main__":
    main()
