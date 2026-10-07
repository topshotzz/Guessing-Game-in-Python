from random import randint
from time import sleep

computer = randint(0, 5)
player = -1   
attempts = 0

while player != computer:
    try:
        player = int(input("try to guess the number I'm thinking of (between 0 and 5): "))
    except ValueError:
        print("please enter a valid number!")
        continue

    attempts += 1
    print("processing...")
    sleep(2)

    if player == computer:
        print(f"congratulations! you guessed it right in {attempts} attempt(s)!")
    else:
        print("sorry, you guessed wrong. try again!")