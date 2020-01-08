#Bales, Greyson
#guess my number game
#10/2019

#imports
import random

#global variables
max_tries = 10
rmin=1
rmax=10

#functions
#makes sure the input is a number
def get_num_in_range(rmin,rmax):
    while True:
        num = input("pick a number between "+str(rmin)+" and "+str(rmax)+"\n")
        if num.isdigit():
            num = int(num)
            if num >= rmin and num <= rmax:
                return num
        print("not a good value")
#runs the game and number of tries
def guess_my_number(rmin,rmax,max_tries):  
    tries = 0
    rnum = random.randint(rmin,rmax)
    guess = get_num_in_range(rmin,rmax)
    tries +=1
    while tries != max_tries and guess != rnum:
        if guess > rnum:
           print("guess lower")

        else:
            print("guess higher")
        guess = get_num_in_range(rmin,rmax)
        tries +=1
    if guess == rnum:
        print("you've won!")
    else:
        print("you've lost")
    print(rnum)
#menu choices
def number_game_menu():
    while True:
        print("""
        MENU
_____________________
    1.Play game
    2.Option menu
    3.Quit
    """)
    
        input_ = input("pick an option \n")
        if input_ == "1":
            guess_my_number(rmin,rmax,max_tries)
        elif input_== "2":
            number_game_options()
        elif input_== "3":
            leave  = input("Are you sure you want to exit?y/n?")
            if leave == "y":
                    exit()
            else:
                    number_game_menu()
        elif input_ == "4":
            computer_guess_number()
        

#options menu
def number_game_options(): 
    while True:
        print("""
        OPTIONS
_______________________
    1.Easy
    2.Medium
    3.Hard
    4.Custom
""")
     #selecting different 
        choice = input("What option would you like to select?")
        if choice == "1":
            rmin = 1
            rmax = 10
            max_tries = 10
            guess_my_number(rmin,rmax,max_tries)
        elif choice == "2":
            rmin = 1
            rmax = 10
            max_tries = 3
            guess_my_number(rmin,rmax,max_tries)
        elif choice == "3":
            rmin = 1
            rmax = 10
            max_tries = 1
            guess_my_number(rmin,rmax,max_tries)
        elif choice == "4":
            rmin = input("What is the minimum number?")
            rmax = input("What is the maximum number?")
            max_tries = input("What is the max number of tries?")
            guess_my_number(rmin,rmax,max_tries)
        


#has the computer play the game























number_game_menu()






























































































































































    
