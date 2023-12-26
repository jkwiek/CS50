import random

def main():
    level = get_level()
    questions_asked = 0
    tries = 1
    score = 0
    while questions_asked < 10:
        question = generate_problem(level)
        problem = question[0]
        solution = question[1]
        while True:
            try:
                user_input = int(input(problem))
                if user_input == solution:
                    questions_asked += 1
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                    print("EEE")
                    if tries < 3:
                        tries += 1
                        continue
                    else:
                        print(problem, solution, sep="")
                        questions_asked += 1
                        break
    print(f"Score: {score}")

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
