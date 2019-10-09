#Bales, Greyson
#10/2019
#lists

import random
top_games = ["Modern Warfare 2",
             "Old School Runescape",
             "Minecraft",
             "League of Legends",
             "Ark",
             "Smash Bros",
             "Forza",
             "Need for speed",
             "MarioKart",
             "Galiga",
             "Pinball",
             "Bloons Tower Defese 5",
             "Bloons Tower Defense 6",
             "Horseshoes, Handguns, and Handgrenades",
             "Subnautica",
             "Faster Than Light",
             "Tetris",
             "Wii Sports",
             "PacMan",
             "Grand Theft Auto 5",
             "Portal"]

last_games = ["Final Fantasy 1",
              "Final Fantasy 2",
              "Final Fantasy 3",
              "Final Fantasy 4",
              "Final Fantasy 5",
              "Final Fantasy 6",
              "Final Fantasy 7",
              "World of Warcraft",
              "BattleFront",
              "BattleFront 2",
              "OverWatch",
              "Hearth Stone",
              "Dungeons & Dragons",
              "Destiny 2",
              "Adventure Capitalist",
              "Mario Party",
              "Pokemon (all of them)",
              "Roblox",
              "RS3",
              "CSGO"]



for i in top_games:
    print(i)














##print(type(top_games))
##
##print(len(top_games))
##print(top_games)
##print(top_games[0:5])
######for i in top_games:
######    print(i)
######for i in range(0,len(top_games)):
######    print(top_games[i])
####num = random.randint(0,len(top_games)-1)
####print(top_games[num])

if len(top_games) < 20:
    print("Fail")
elif "Fortnite" in top_games or "fortnite" in top_games:
    print("Fail")
elif top_games[0] != "Modern Warfare 2":
    print("Fail")
else:
    print("Pass")

for i in top_games:
    if i == "Modern Warfare 2":
        print("I found it")
    else:
        print("Not it")


top_games[5] = "updated"
####print(top_games)
