# import random
import os


# def chooseWord():
#     index = random.randint(1, 171)



def run():
    playing = 1
    while True:
        playing = int(input("Do you want to playing yet ? \n0.No \n1.Si\n"))
        if playing != 1:
            break
        os.system("clear")


if __name__ == '__main__':
    run()