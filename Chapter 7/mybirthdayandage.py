import datetime


#for the users input
birthday_string = input("Please enter your birthday YYYY-MM-DD: ")

#making that input correct
my_birthday = datetime.datetime.strptime(birthday_string,"%Y-%m-%d")

print(my_birthday.strftime("%x"),"Is your birthday")
print("You where born on a",my_birthday.strftime("%A"))

now = datetime.datetime.now()

age = now-my_birthday

years = age.days/365

print(str.format("you are {:.10f} years old", years))
