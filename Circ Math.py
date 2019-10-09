msr_sqr_side = input("What's your measurement? ie feet, meter ")

#side length
sqr_side_length = input("What's your side length? ")


#equation and variable for that answer

area_sqr = float(sqr_side_length) * float(sqr_side_length)

#giving answer back formated to 2 decimals

form_area_sqr = str.format(" :{0:15.2f}", area_sqr)

#print(form_area_sqr , msr_sqr_side , "squared")




#ascii art of a square for a representative


sqr_area = str.format("""
 ___{:^5.3g}__
|         |
|         |
|    {:^5.3g}|
|         |
|_________|""", float(sqr_side_length) , float(sqr_side_length))


print( sqr_area)
input()
