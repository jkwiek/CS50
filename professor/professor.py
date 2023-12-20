import random

def main():
    get_level()
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
    integer = random.getrandbits(level)
    print(integer)



if __name__ == "__main__":
    main()
