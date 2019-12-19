import random
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
######def picked_question(words, questions):
######    number_list = []
######    picked = random.randint(0,len(words)-1)
######    while picked not in number_list:
######        picked = random.randint(0,len(words)-1)
######        number_list.append(picked)
######    asked_words = words.pop(picked)
######    asked_question = questions.pop(picked)    
######    return asked_question, asked_words
######    asked_question, asked_words = picked_question(words, questions)
######    print(asked_question)


##############################################################
    #taken out of QA Q_and_A(puzzle,words,questions,picked): Q_and_A(words,questions):
def Q_and_A(words,questions):
    import random
    picked=[]
    while True:
        pick=random.randint(0,len(words)-1)
        if pick not in picked:
            q=questions[pick]
            a=words[pick]
            picked.append(pick)
            return q, a














