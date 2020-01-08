#Greyson Bales
#1/2020
#Pig Latin Translator
# initialize size variable
size = 0

# get and validate user size input
while True:
    try:
        size = int(input("Please enter the number of characters to move to the end (1 - 3): "))
        if (size >= 1) and (size <= 3):  # validate range
            break;  # we're good, exit loop
        else:
            print("Try again")
    except:
        print("Try again")

# get input string we want to transform
sentence = input("Please enter a word, phrase or sentence: ")

# break string into list of individual words
words = str.split(sentence)  # break sentence into words

# initialize empty pig latin version of the input sentence
piglatin = ""

# for each word, convert and build piglatin output
for word in words:
    word = str.lower(word)  # convert word to lower case
firstChar = word[0]  # get first character to examine

if (firstChar in "aeiou"):  # If the first letter is a vowel
# add the letters "\way" to the end of the word.
    word = word + "\\way"
else:  # else the first letter is a consonant
# break the word into 2 pieces at the "size" index
    firstPart = word[:size]
    lastPart = word[size:]
# build new word by starting with the last part, adding a backslash,
# then the first part, then the characters "ay" at the end
word = lastPart + "\\" + firstPart + "ay"

# add the new word to the end of the pig latin string, plus a space
piglatin = piglatin + word + " "

# print the original and final results!
print(sentence)
print(piglatin)