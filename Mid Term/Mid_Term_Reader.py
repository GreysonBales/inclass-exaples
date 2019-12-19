# Bales, Greyson
# 12/19
# midterm


import sys

def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        return file
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()



def next_line(the_file):
    line = the_file.readline()
    line = line.strip("\n")
    line = line.replace("/","\n")
    return line


def question_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        line = next_line(the_file)
        answers.append(line)
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation
    

def welcome(title):
    """Welcoming the player and getting hir/her name."""
    print("\t\tWelcome to my python Trivia Challenge!")
    print("\tThis test was created by",title,"\n")




def report_card(name, question_count, score):
    """Gives the user there score in percent and how many out of how many
        they got correct."""
   
    username = name
    questions = question_count
    correct = score

    point_per_ques = 1 / questions
    points_1 = point_per_ques * score
    points_2 = points_1 * 100


    grade = str.format("""






            REPORT CARD
Name = {0}
Points per a question = {1}
Number of questions = {2}
You scored a {3}
Good job!!







""",username,point_per_ques, questions, points_2)
    print(grade)
    write_score(username, points_2)
    


def get_file_name():
    while True :
        file_name = input(" Enter the name of your file including the .txt")
        if ".txt" in file_name and " " not in file_name:
            return file_name
        else:
            print("you're a bryan")



def write_score(name,score):
    file = open_file("scores.txt","a+")
    pair = name+" :      " + str(score) + "\n"
    line = []
    line.append(pair)
    file.writelines(line)
    file.close()





def main():
    file_name = get_file_name()
    the_file = open_file(file_name, "r")
    title = next_line(the_file)
    name = input("please give me your full name")
    question_count = 0
    score = 0
    category, question, answers, correct, explanation = question_block(the_file)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
            print("\t", i + 1, "-" , answers[i])
        user_answer = input("\n Please select the correct answer(1,2,3,4)")
        if user_answer == correct:
            print("You're correct!!")
            score +=1
            question_count += 1
        else:
            print("You're incorrect")
            question_count+= 1
        print()
        print(explanation)
        category, question, answers, correct, explanation = question_block(the_file)
    the_file.close()
    print("file has closed")
    input("press enter to see the report card")
    report_card(name, question_count, score)
            
            
    







main()
input("press enter to close")















