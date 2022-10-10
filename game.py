from random import randint
from itertools import count

playerName = (input("Lets play a number guessing game! What is your name?\n"))

def number_guessing(minimum, maximum):
    randomNum = randint(minimum, maximum)
    for tries in count(1):
        numPlayer = int(input("Guess a number between ({}-{}) \n".format(minimum, maximum)))
        if numPlayer > randomNum:
            print ("Too high, try again!")
        elif numPlayer < randomNum:
            print ("Too low, try again!")
        elif numPlayer == randomNum:
            return tries

print ("Well done,", playerName, "you guessed my number in {} guesses!".format(
    number_guessing(1, 100)))