#Bales, Greyson
import random


#player stat
deff = 0
atk = 1
health = 100
mana = 10
inv = []
equp = []
max_inv = 10

#items in chests
chest_inv = ("gold",
             "gems",
             "food",
             "rusty butter knife",
             "armour",
             "shield",
             "healing potions",
             "mana potion",
             "arrows",
             "Broken Shortbow",
             "Spear",
             "Cross bow",
             "Helm",
             "pants",
             "Boots",
             "Spork",
             "Doom Hammer",
             "Orb of Future telling",
             "Twisted bow",
             "gloves",
             "Bracers",
             "Glaces")
max_chest = 15
items = random.randint(1, max_chest)
chest = []
for i in range(items):
    chest.append(random.choice(chest_inv))

input("press enter to open chest")
for i in chest:
    inv.append(i)
if len(inv) > max_inv:
    x = len(inv) - max_inv
    print(inv)
    print("you need to remove "+str(x)+" items")
    while x > 0:
        item = input("What item(s) do you want to remove?")
        inv.remove(item)
        x-=1
    print(inv)
#Checking inv
if inv:
    print(inv)
else:
    print("You... Are... Nothing")
    input("open the chest to get your item")
    for items in chest:
        inv.append(items)


print(inv)

for items in inv:
    if items == "healing potions":
        health += 50
        inv.remove("healing potions")







#defence items

for items in inv:
    if items == "armour":
        deff+=10
        equp.append("armour")
        inv.remove("armour")
for items in inv:       
    if items == "shield":
        deff+=10
        equp.append("shield")
        inv.remove("shield")
for items in inv:       
    if items == "Helm":
        deff+=3
        equp.append("Helm")
        inv.remove("Helm")
for items in inv:        
    if items == "pants":
        deff+=100
        equp.append("pants")
        inv.remove("pants")
for items in inv:     
    if items == "boots":
        deff+= -2
        equp.append("boots")
        inv.remove("boots")
for items in inv:        
    if items == "gloves":
        deff+=1
        equp.append("gloves")
        inv.remove("gloves")
for items in inv:        
    if items == "Bracers":
        deff+=6
        equp.append("Bracers")
        inv.remove("Bracers")
for items in inv:        
    if items == "Glasses":
        deff+=100
        equp.append("Glasses")
        inv.remove("Glasses")
        
    
print(health)
print(deff)
print(inv)
