#bales greyson
#word search
#12/2019
#word search for made from words out of python words.

#imports
import random



#the puzzle
puzzle="DKOWZFLOWCHARTQINZYYVXMPCBMOBBPFCCSHWYJGOOGLEXSSOJTALFKKWKOFYZUTNAIRANDINTIYCGCACOXYXHGKSLPFORSTATEMENTWEAIQBRIETAPPENDERNVIAMPMEMYXPWSATINNPRCENNTEVTMEDADOICONARHEREGERORNXVPTTEOITENYMTTXJBYYISNERBOOLEANFFHCOGRBRYANSHUFFLEBN&rlz=1C1GCEA_enUS863US863&oq=DKOWZFLOWCHARTQINZYYVXMPCBMOBBPFCCSHWYJGOOGLEXSSOJTALFKKWKOFYZUTNAIRANDINTIYCGCACOXYXHGKSLPFORSTATEMENTWEAIQBRIETAPPENDERNVIAMPMEMYXPWSATINNPRCENNTEVTMEDADOICONARHEREGERORNXVPTTEOITENYMTTXJBYYISNERBOOLEANFFHCOGRBRYANSHUFFLEBN"
p = puzzle





#words for the puzzle and questions to go with those words, in order together.
words = [ "PYTHON",
        "IMPORT",
        "PRINT",
        "INTEGER",
        "RANDOM",
        "IFSTATEMENT",
        "FORSTATEMENT",
        "APPEND",
        "FILE",
        "RANDINT",
        "BINARY",
        "COPY",
        "CONCATENATION",
        "PARAMETER",
        "IDE",
        "GOOGLE",
        "FLOWCHART",
        "STRING",
        "BOOLEAN",
        "SHUFFLE",
        "BRYAN"]
questions = [ "What language do we use to create this program.",
            "To bring code from another file.",
            "Displays whatever is in it.",
            "Is only a whole number.",
            "Is a import to choose anything at ______ .",
            "This checks to make sure the variable completes a certain checklist.",
            "This checks to make sure that it only repeats for a certain amount of time.",
            "Adds the variable to the list.",
            "you normally import a ____.",
            "This function chooses a random integer.",
            "Computers use it, also base 2.",
            "makeing an iditical copy of something, or ctrl-c.",
            "the action of linking things together in a series.",
            "Is any characteristic that can help in defining or classifying a particular system.",
            "What is idle or a source code editor.",
            "Most commonly used search engine.",
            "We use these to plan out our program before building.",
            "Has quatations around it, either single or double.",
            "What data type has only two possible values, True or False.",
            "A lot of people put there music on _______.",
            "The biggest meme of the class python period 4-5."] 









#start of the functions
##########################################################################################


#puzzle grid to display the puzzle with the letters in it for a 15x15
def display_puzzle5(p):
    grid = str.format("""
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
  ------------------------------------------------------------
0 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
1 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
2 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
3 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
4 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
5 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
6 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
7 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
8 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
9 | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
10| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
11| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
12| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
13| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
14| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
  ------------------------------------------------------------
""",p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13],p[14],p[15],p[16],
p[17],p[18],p[19],p[20],p[21],p[22],p[23],p[24],p[25],p[26],p[27],p[28],p[29],p[30],p[31],p[32],p[33],p[34],p[35],p[36],
p[37],p[38],p[39],p[40],p[41],p[42],p[43],p[44],p[45],p[46],p[47],p[48],p[49],p[50],p[51],p[52],p[53],p[54],p[55],p[56],
p[57],p[58],p[59],p[60],p[61],p[62],p[63],p[64],p[65],p[66],p[67],p[68],p[69],p[70],p[71],p[72],p[73],p[74],p[75],p[76],
p[77],p[78],p[79],p[80],p[81],p[82],p[83],p[84],p[85],p[86],p[87],p[88],p[89],p[90],p[91],p[92],p[93],p[94],p[95],p[96],
p[97],p[98],p[99],p[100],p[101],p[102],p[103],p[104],p[105],p[106],p[107],p[108],p[109],p[110],p[111],p[112],p[113],p[114],p[115],p[116],
p[117],p[118],p[119],p[120],p[121],p[122],p[123],p[124],p[125],p[126],p[127],p[128],p[129],p[130],p[131],p[132],p[133],p[134],p[135],p[136],p[137],
p[138],p[139],p[140],p[141],p[142],p[143],p[144],p[145],p[146],p[147],p[148],p[149],p[150],p[151],p[152],p[153],p[154],p[155],p[156],p[157],
p[158],p[159],p[160],p[161],p[162],p[163],p[164],p[165],p[166],p[167],p[168],p[169],p[170],p[171],p[172],p[173],p[174],p[175],p[176],p[177],
p[178],p[179],p[180],p[181],p[182],p[183],p[184],p[185],p[186],p[187],p[188],p[189],p[190],p[191],p[192],p[193],p[194],p[195],p[196],p[197],
p[198],p[199],p[200],p[201],p[202],p[203],p[204],p[205],p[206],p[207],p[208],p[209],p[210],p[211],p[212],p[213],p[214],p[215],p[216],p[217],
p[218],p[219],p[220],p[221],p[222],p[223],p[224],p[225])
    print(grid)


#getting a question and adding it to an already picked list
def Q_and_A(words,questions):
    import random
    picked=[]
    while True: #making sure the word isnt already on the list of chosen words
        pick=random.randint(0,len(words)-1)
        if pick not in picked:
            q=questions[pick]
            a=words[pick]
            picked.append(pick)
            return q, a



# p taken out of word math 2 from very begging
def word_math2(a,puzzle):
    nums = []#blank list to keep track of numbers
    print("so get the correct index pos,\ntake the vertical number times 15 and add the horizontal")#how to get index pos.
   
    for i in a:#loops for how many letters are in the word
        guess = input("what number would you like to choose your word is "+str(len(a))+" letters long\n that's how many imputs you will have")#asks for the letter pos in the index
        if guess.isdigit():
            
            print("good choice, please choose another \n\n")#is it a digit, if so nice choice
            nums.append(int(guess))
        else:
            print("bad choice, please choose a different number\n\n")#it's not a digit choose again
    if nums[0]+1 == nums[1] or nums[0]+15==nums[1] or nums[0]-15==nums[1] or nums[0]+16==nums[1] or nums[0]-16==nums[1]:
#making sure the number is within the correct number of spaces, if not it will break
        word = ""
        while nums:
            x = nums.pop(0)
            word = word +puzzle[x]
        return word 
    print(nums)
       



    



##display_puzzle5(p)
##q,a = Q_and_A(words,questions)
##print(q)
##word = word_math2(a,puzzle)
##print(word)



def main(p,words,questions,a,puzzle):

    score = 0
    while True in range(1,20):
        display_puzzle5(p)
        q,a = Q_and_A(words, questions)
        print(q)
        print("\n\n\n")
        word = word_math2(a,puzzle)
        if word == a:
            print("\n\n\n Good job you scored a point, continue to play!")
            score +=1
        else:
            print("\n\n\n Nice, you done failed. Here's your score card.")
            break
        print("Way to play the word search!")
        print("you scored \n\n\n\n " , score,"\n\n\n\ Way to go!"





















main(p,words,questions,a,puzzle)



































    
