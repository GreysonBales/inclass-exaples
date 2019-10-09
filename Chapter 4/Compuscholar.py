#bales greyson
#compuscholar stuff

mood = "happy"

grade= 10
age = 17
minimum_age = 16
has_car = True
users = ["eric","bob","tim","jen"]
password= 1234

result1 = (mood == "happy") and (age>= 18 or has_car)
result2 = not((age-minimum_age)>0)
result3 = has_car or (age<(grade*2))
result4 = "eric" in users and password != 1234

print("result1 =" , result1)
print("result2 =" , result2)
print("result3 =" , result3)
print("result4 =" , result4)
