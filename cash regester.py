#Bales, Greyson
#9/9/19
#cash register



#Declaring Variables



num_items = 5 

cost_per_item = 10

taxes = .08

#Mathmatical Variables

sub_total = num_items * cost_per_item

tax_amount = taxes * sub_total

total_price = tax_amount + sub_total


#printing all the receipts


print("SALES RECEIPT")
print(" ")

print("Number of items  " + str(num_items))
print(" ")
print("Item cost        " + "$" + str(cost_per_item))
print(" ")
print("Sub total        $" + str(sub_total))
print(" ")
print("Total Taxes      $" + str(tax_amount))
print(" ")
print("______________________")
print(" ")
print(" ")
print("Total sales      $" + str(total_price))








#refrence points
#SALES RECEIPT
#Number of items : 5
#Cost per item   : $5.5
#Tax rate        : 0.06
#Tax amount      : $1.65
#TOTAL SALE PRICE: $29.15
