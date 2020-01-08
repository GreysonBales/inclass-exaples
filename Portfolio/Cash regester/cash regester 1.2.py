#Bales, Greyson
#9/9/19
#cash register



#Declaring Variables



num_items = input("How many items do you have?") 

cost_per_item = input("What was the cost per an item?")

taxes = input("how much is your taxes from where your from? *ie .08")

#Mathmatical Variables

sub_total = num_items * cost_per_item

tax_amount = taxes * sub_total

total_price = tax_amount + sub_total


#printing the receipt

#seperator variable
sep1 = "$"
print("---SALES RECEIPT---")
print(" ")
print("Number of items   " , num_items )
print(" ")
print("Item cost        " , cost_per_item , sep=sep1)
print(" ")
print("Sub total        " , sub_total , sep=sep1)
print(" ")
print("Total Taxes      " , tax_amount , sep=sep1)
print(" ")
print("______________________")
print(" ")
print("Total sales      " , total_price , sep=sep1)

input()
