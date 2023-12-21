import random

def main():
    level = get_level()
    number1 = generate_integers(level)
    number2 = generate_integers(level)
    problem = f"{number1} + {number2} = "
    answer = input(problem)
    solution = int(number1) + int(number2)
    print(solution)

    #for problems <= 10:
        #number= generate_integers(level)
        #solution = number + generate_integers(level)


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
    digit = str(random.randint(1,9))
    integer += [digit]
    for _ in range(level-1):
        digit = str(random.randint(0,9))
        integer += [digit]
    integer = "".join(integer)
    return integer

if __name__ == "__main__":
    main()
