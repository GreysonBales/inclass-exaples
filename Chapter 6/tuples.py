#Bales, Greyson

highscores = [100,90,80,70,60,50,40,30,20,10]
print(len(highscores))
print(max(highscores))
print(min(highscores))


var=5,4,3,2,1
for number in var:
    highscores.append(number)
 


score = 99
highscores.insert(1,score)
print(highscores)

highscores.remove(99)
print(highscores)
hand = highscores.pop(len(highscores)//2)
print(hand)



######################highscores.clear()
######################print(highscores)
x = highscores.index(50)
print(x)
print(highscores.count(100))
highscores.sort(reverse = True)
print(highscores)
