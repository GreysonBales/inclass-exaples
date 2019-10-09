#Bales, Greyson
#9/25/19
#get name


def get_name():
    while True:
     name = input("What's your name?")
     if " " in name:
         name = name.replace(" ","QZRX")
     if name.isalpha():
        name = name.replace("QZRX"," ")
        name = name.title()
        return name
     else:
        print("invalid syntax, try again")

def math_fun(x,y):
    if x.isdigit()and y.isdigit()and len(x) <=2 and len(y) <= 3:
        x=int(x)
        y=int(y)
    else:
        pirnt("invalid syntax")
    num1 = x
    num2 = y
    total = num1*num2
    return total
x = input("enter a number for x ")
y = input("enter a number for y ")



result = math_fun(x,y)
print(result)
