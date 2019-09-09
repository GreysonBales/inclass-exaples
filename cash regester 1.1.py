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


#printing the receipt


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

