import random
import os


# Con esto creo la lista de palabras para el juego
def getListOfWords():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        return  [i for i in f]


def chooseWord():
    return random.randint(1, 172)


def chooseDifficulty(length):
    # Pido que el jugador elija una dificultad
    difficulty = input("1.Easy\n2.Normal\n3.Hard\n")
    # Me aseguro de que la dificultad sea valida
    assert difficulty.isnumeric(), "Excuse us, the chosen difficulty doesn't exist"
    difficulty = int(difficulty)
    if difficulty == 3:
        return length * 2
    elif difficulty == 2:
        return length * 3
    else:
        return length * 4


def printLetters(word, letter):
    pass


def game(word, attempts):
    while attempts > 0:
        letter = input("Type a letter: ")
        if word.find(letter) == -1:
            print("Ups!, that letter don't is in word")
            attempts = attempts - 1
        else:
            printLetters(word, letter)


def run():
    os.system("clear")
    playing = 1
    words = getListOfWords()

    while True:
        print("Welcome to El Ahorcado\nChoose a difficulty")
        index = chooseWord()
        word = words[index]
        attempts = chooseDifficulty(len(word))

        if game(word, attempts):
            print("You Win!!!")
        else:
            print("You Loose:(")

        playing = input("Do you want to playing yet ? \n0.No \n1.Si\n")
        assert playing.isnumeric(), "Excuse us, invalid value"
        playing = int(playing)
        if playing != 1:
            break
        os.system("clear")


if __name__ == '__main__':
    run()