import random


def main():
    a = get_level()
    score = generate_integer(a)
    print(f"Your score is {score}/10")


def get_level():
    while True:
        try:
            level = int(input("Enter the level (1,2,3) : "))
            if level!=1 and level!=2 and level!=3:
                raise ValueError("Please indicate a specified level!")
            else:
                break
        except ValueError:
            print("Please indicate level 1, 2, 3 ")
    return level



def generate_integer(level):
        counter = 10
        mistake_counter = 0
        correct_answer = 0
        while counter > 0:

            x = random.randint(1,10** level-1)
            y = random.randint(1, 10**level-1)
            result = (input(f"{x} + {y} = "))
            try:
                result =int(result)
            except ValueError:
                print("EEE")
                continue

            if (x + y) == result:
                correct_answer+=1
                counter-=1
            else:
                print("EEE")
                mistake_counter+=1
                counter -=1
                if mistake_counter==3:
                    print(f"The correct answer is {x+y}")
                else:
                    print("Try Again!")
        return correct_answer




if __name__ == "__main__":
    main()