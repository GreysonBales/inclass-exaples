
#computer variables coming in as strings
cmin = input("min")
cmax = input("max")
ctries = input("tries")
cnumber = input("number")
#changing to ints
cmin = int(cmin)
cmax = int(cmax)
ctries = int(ctries)
cnumber = int(cnumber)
#computer guessing

while True:

    cguess = cmax/2
    print(cguess)
    if cguess == cnumber:#win
        print("computer wins")
        break
    elif cguess < cnumber:#guess higher
        cmin = cguess
    elif cguess < cnumber:#guess lower
        cmax = cguess
