#bales, greyson
#9/25/19
#coinflip
import random
def coin_flip(x):
    
    if x.isdigit():
        x=int(x)
    if x > 0:
        for i in range(x):
            side = random.randint(1,2)
        if side == 1 :
            print("heads")
        else :
            print("tails")
    else:
        print("I'm broken")
numb_flips = input("how many times would you like to flip?")
coin_flip(numb_flips)

print(coin_flip)
