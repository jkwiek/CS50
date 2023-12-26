import random

def main():
    level = get_level()
    questions_asked = 0
    tries = 1
    while questions_asked<10:
        problem = generate_problem(level)[0]
        solution = generate_problem(level)[1]
        if input(problem) == solution:
           questions_asked =+ 1
           continue
        else:
            while tries <= 3:
                print("EEE")
                tries=+1
            print(solution)
            questions_asked=+1
            



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

def generate_problem(level):
    number1 = generate_integers(level)
    number2 = generate_integers(level)
    solution = int(number1) + int(number2)
    problem = f"{number1} + {number2} = "
    return problem, solution



if __name__ == "__main__":
    main()
