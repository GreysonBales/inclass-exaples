#Bales, Greyson
#guess my number game
#10/2019


import random
from GuessFunction import *

max_tries = 10
rmin=1
rmax=10


def number_game_menu():
    print("""
        MENU
_____________________
    1.Play game
    2.Option menu
    3.Quit
    """)
    input = input("pick an option \n")
    if input == "1":
        guess_my_number(rmin,rmax,max_tries)
    elif input== "2":
        number_game_options()
    elif input== "3":
        leave  = input("Are you sure you want to exit?y/n?")
            if leave == "y":
                exit()
            else:
                number_game_menu()
    

    
