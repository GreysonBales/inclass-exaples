#read and write to a file

import pickle,shelve
variety = ["sweet","hot","dill","bread and butter"]
shape = ["whole","spear","chip"]
brand = ["Claussen","Heinz","Vlassic"]

##f = open("pickles1.dat","wb+")
##pickle.dump(variety, f)
##pickle.dump(shape, f)
##pickle.dump(brand, f)
##f.close()
##
##f = open("pickles1.dat","rb+")
##brand = pickle.load(f)
##shape = pickle.load(f)
##variety = pickle.load(f)
##
##print(variety)
##print(shape)
##print(brand)
##
##f.close()


s = shelve.open("pickles2.dat")
s["variety"] = ["sweet","hot","dill","bread and butter"]
s["shape"] = ["whole","spear","chip"]
s["brand"] = ["Claussen","Heinz","Vlassic"]
s.sync()

print("brand ",s["brand"] )
print("shape -", s["shape"])
print("variety -", s["variety"])

s.close()










##readme = "highscores.txt"
##
##def read_word(file,sep):
##    """Reads a file up to the given seperator"""
##    word = ""
##    letter = ""
##    while letter != sep:
##        letter = file.read(1)
##        word +=letter
##    print(word)
##
##tf = open("highscores.txt","r+")
##bryans_scores = tf.readlines()
##print(bryans_scores)
##clean_list= []
##for i in range (len(bryans_scores)):
##    x = bryans_scores[i].strip()
##    clean_list.append(x)
##print(clean_list)
##
##tf.writelines(clean_list)
##print(tf.read())
##tf.close()
##
