#blaes, greyson
#hangman
#10/19


#trying to build the classic game of hangman.
#computer picks word
#the player guesses it
#one letter at a time
#can't figure it out in time, you die.

#imports
import random

#constants
HANGMAN = ('''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''')



MAX_WRONG = len(HANGMAN) - 1

WORDS = ("HELLO","PYTHON","RACHEL")

# initialize variables
word = random.choice(WORDS) #the word to be guessed
so_far = "-" * len(word) #dashes for words
wrong = 0 #number us guesses the player has made wrong
used = [] #What letters the player has used 

#welcoming the player
print("Welcome to hangman, hopefully you don't die. GOOD LUCK!")

#game loop

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print("\nYou've used the folling letters:\n",used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed this letter", guess)
        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nYES!", guess, "is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")
print("the word was", word)
input("\n\nPress the enter key to exit.")



























