user_name = input("What is your name?")
print("Welcome " + user_name)

user_age = input("How old are you")


try:
    print("You will be" , int(user_age) + 5 , "in 5 years")
    print("You are" , user_age , "years old")

except:
    print("You absoulte BAFOON!! That wasen't a number")
