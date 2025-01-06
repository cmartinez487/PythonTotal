#Proyecto Dia 5 - El Ahorcado
import random
from os import system
wordsList = ["Cholo", "Traqueto", "Cotorro", "Paralelepipedo", "aguevoneado"]

def ValidateLetter():
    abc = 'abcdefghijklmnopqrstuvwxyz'
    isValid = False
    letter = ''
    while not isValid:
        letter = input("Elige una letra ").lower()
        if letter in abc and len(letter) == 1:
            isValid = True
        else:
            system('clear')
            print("Suministraste un caracter valido, por favor elige una letra ")

    return letter

def LostLife(lifePlayer):
    if lifePlayer > 0:
        lifePlayer -= 1

    return lifePlayer

def SelectWord():
    selectedWord = random.choice(wordsList)
    return selectedWord

def ContructHangmanList(counterWord):
    hangMan = []
    while counterWord != 0:
        hangMan.append("-")
        counterWord -= 1
    return hangMan

def SuccessWordHangmanList(letter, selectedWord, hangman):
    for i in range(len(selectedWord)):
        print(i)
        if selectedWord[i] == letter:
            hangman[i] = letter
    return hangman

def PlayTheGame(selectedWord:str):
    again = 1
    lifePlayer = 6
    counterWord = len(selectedWord)
    hangman = ContructHangmanList(counterWord)

    while again != 0:
        print(hangman)
        letter = ValidateLetter()
        isFound = letter in selectedWord

        system('clear')

        if isFound:
            hangman = SuccessWordHangmanList(letter, selectedWord, hangman)
            counterWord -= selectedWord.count(letter)
            if counterWord == 0:
                print(f"Haz encontrado todas las Letras!!! la palabra es {selectedWord}")
                input()
                break

            print(f"Encontrada la letra {letter}")
        else:
            lifePlayer = LostLife(lifePlayer)
            if lifePlayer == 0:
                again = 0
                print(f"Has perdido. La palabra era {selectedWord}.")
            else:
                print(f"No encontrada la letra {letter}. Te quedan {lifePlayer} vidas")
                again = int(input("¿Quieres seguir jugando? "))
                system('clear')

def HangManGame():
    print(f'Bienvenidos al Juego del Ahorcado')
    againSelect = int(input("Pulsa 1 para jugar o 0 para salir "))
    system('clear')

    while againSelect == 1:
        system('clear')
        selectedWord:str = SelectWord()
        PlayTheGame(selectedWord.lower())
        againSelect = int(input("¿Deseas jugar de nuevo? "))

    system('clear')
    print(f'Game Over')

HangManGame()
