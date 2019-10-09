def intro(name):
    print("""

    Welcome to """+name+"""
    please chose an option
    from the list below

    1: option 1
    2: option 2
    3: option 3
    4: quit
    """)

def option1():
    print("option 1")
def option2():
    print("option 2")
def option3():
    print("option 3")
def option4():
    varify = input("Are you sure you want to quit?")
    varify = varify.lower()
    if "y" in varify:
        return True
    else:
        return False

def menu():
    while True:
        intro("example")
        choice = input("Pick an option; 1.2.3. or 4")
        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            varify = option4()
            if varify :
                break
            else:
                continue
        else:
            print("That's not an option")



menu()
input("press enter to exit")
