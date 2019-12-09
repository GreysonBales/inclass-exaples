#Bianary search
#bales, greyson
#11/2019
num = 8
low = 1
high = 11


def comp_guess(low,high):
    num_list = []
    for i in range(low,high+1):
        num_list.append(i)
    choice = len(num_list)//2
    
    return choice+1




choice = comp_guess(low,high)
while choice != num:
    if choice > num :
        print(choice)
        high = choice
    else:
        low = choice
        print(choice)
    input()
    choice = comp_guess(low,high)
if choice == num:
    print("win")
else:
    print("you loose")
    
