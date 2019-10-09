#Bales,Greyson
#10/2019
#Worst games

last_games = ["Final Fantasy 1",
              "Final Fantasy 2",
              "Final Fantasy 3",
              "Final Fantasy 4",
              "Final Fantasy 5",
              "PUBG",
              "Fortnite",
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



for i in last_games:
    print(i)

num = random.randint (0 , len(last_games)-1)
print(last_games[num])
