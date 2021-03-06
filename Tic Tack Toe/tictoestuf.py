#bales, greyson
#tic tac toe
#11/19

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE ="TIE"
NUM_SQUARES = 9



# intro is working!!
def intro():
    """ display game instructions """
    print(
        """
    wlecome to the greatest intellectual challenge of all time: tic-tac-toe.
    this will be a showdown between your human brain and a silicon processor.

    you will make your move known by entering a number, 1-9. The number
    will correspond to the board position as illustraded:

                1 | 2 | 3
                ---------
                4 | 5 | 6
                ---------
                7 | 8 | 9

    prepare yourself, human. The ultimate battle is about to begin

    """
        )

#new board working
def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """display game board on screen"""
    print(str.format("""
            {0} | {1} | {2}
            ---------
            {3} | {4} | {5}
            ---------
            {6} | {7} | {8}
    
""", board[0],board[1],board[2],
     board[3],board[4],board[5],
     board[6],board[7],board[8]))

    
# question is working
def ask_yes_no(question):
    """ ask a yes or no question, with a one letter response back"""
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    x = response[0]
    return x

# ask number is working
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except:
            print("You ignorant slut.\n Choose a number.") 
    return response


#assign peice is working
def assign_piece():
    go_first = ask_yes_no("Would you like to go first?\n")
    if go_first == "y":
        player = X
        comp = O
        print("you are x's and the computer is o's")
    elif go_first == "n":
        comp = X    
        player = O
        print("you are o's and the computer is x's")
    return comp,player


#switch turn works    
def switch_turn(turn):
    if turn == X:
        return O
    else:
        return X
    


#legal moves workds
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


#should be working
def player_turn(board,player):
    lm = legal_moves(board)
    move = None
    while move not in lm:
        move = ask_number("pick a number between 1-9: ", 1, 10)-1
        if move not in lm:
            print("you imbecile, you can't choose that!")
    print("Fine...")
    return move




def winner(board):
    """ Determines the game winner."""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None



#broabents
def comp_turn(board,comp,player):
    copy_board = board[:]

    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    
    print("I shall take square number", end=" ")

    for move in legal_moves(board):
        copy_board[move] = comp
        if winner(copy_board) == comp:
            print(move)
            return move
        copy_board[move] = EMPTY
        
    for move in legal_moves(board):
        copy_board[move] = player
        if winner(copy_board) == player:
            print(move)
            return move
        copy_board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
#mine
##def comp_turn(board, comp, player):
##    copy_board = board[:]
##    BEST_MOVES = (5,1,3,7,9,2,4,6,8)
##    print("I shall take square number", end = " ")
##
##    for move in legal_moves(board):
##        copy_board[move] == comp
##        if winner(copy_board) == comp:
##            print(move)
##            return move
##
##    for move in legal_moves(board):
##        copy_board[move] = player
##        print("test")
##        if winner(copy_board) == player:
##            print(move)
##            return move
##
##    for move in BEST_MOVES:
##        if move in legal_moves(board):
##            print(move)
##            return move
        

def tictacgame():
    turn = X
    intro()
    board = new_board()
    display_board(board)
    comp , player  = assign_piece()
    while not winner(board):
        if turn == player:
            move = player_turn(board,player)
            board[move] = player
        else:
            move = comp_turn(board,comp,player)
            board[move] = comp
        display_board(board)
        turn = switch_turn(turn)
    winer = winner(board)
    if winer == comp:
        print("you suck the computer beat you")
    elif winer == TIE:
        print("you suck, the computer basically beat you")
    elif winer == player:
        print("some how your idiotic self won.")

        










tictacgame()
input()
##board= new_board()
##board[0] = X
##board[1] = EMPTY
##board[2] = X
##board[3] = X
##board[4] = X
##board[5] = O
##board[6] = O
##board[7] = EMPTY
##board[8] = O
##display_board(board)
##win = winner(board)
##print(win)
##move = comp_turn(board,X,O)
##board[move] = X
##display_board(board)






        
        






























