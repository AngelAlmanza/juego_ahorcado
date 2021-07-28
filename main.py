# import random
import os


# def chooseWord():
#     index = random.randint(1, 171)


def chooseDifficulty(length):
    difficulty = input("1.Easy\n2.Normal\n3.Hard\n")
    assert difficulty.isnumeric(), "Excuse us, the chosen difficulty doesn't exist"
    difficulty = int(difficulty)
    if difficulty == 3:
        return length + 3
    elif difficulty == 2:
        return length + 6
    else:
        return length * 2


def run():
    playing = 1
    while True:
        print("Welcome to El Ahorcado\nChoose a difficulty")
        attempts = chooseDifficulty(6)
        print(attempts)
        playing = int(input("Do you want to playing yet ? \n0.No \n1.Si\n"))
        if playing != 1:
            break
        os.system("clear")


if __name__ == '__main__':
    run()