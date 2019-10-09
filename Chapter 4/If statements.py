#Bales, Greyson
#9/23/19
#???


user_names = "Greyson, bob, tim, steve, trump"
password = "password"

user = input("Enter your username ")
user_pass = input("Enter your password ")


if user in user_names:
    if user_pass in password :
        print(user_name , "is signed in")
    else:
        print("wrong password")
elif user != user_name:
    print("Not a good user name")

else:
    print("My mom told me not to talk to strangers")
