#Bales, Greyson
#Guess my number function
#10/2019

# Gets a number, is actually a number, and in the range, then returns number
def get_num_in_range(rmin,rmax):
    while True:
        num = input("pick a number between "+str(rmin)+" and "+str(rmax)+"\n")
        if num.isdigit():
            num = int(num)
            if num >= rmin and num <= rmax:
                return num
        print("not a good value")

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
