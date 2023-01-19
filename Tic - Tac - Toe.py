import random

#Function used to print the board

def render(cells):

    print("The board")
    print(cells[0], "|", cells[1], "|", cells[2])
    print("--+---+--")
    print(cells[3], "|", cells[4], "|", cells[5])
    print("--+---+--")
    print(cells[6], "|", cells[7], "|", cells[8])

#Function to take user input

def userInput(board, mark):

    spot = ''

    while not(spot in ['1','2','3','4','5','6','7','8','9'] and board[int(spot)-1] == ' '):

        spot = input("\nEnter your move: ")

    pointer = int(spot) - 1

    newBoard = board[:pointer] + mark + board[pointer+1:]

    return newBoard

#Algorithm that selects best possible moves

def computerInput(board, mark):

    pointer = ''

    lboard = ''

    for x in board:

        if x == " ":

            lboard = lboard + " "

        elif x == mark:

            lboard = lboard + "."

        else:

            lboard = lboard + "?"

    if(lboard == "         "
    or lboard == "?        " or lboard == "  ?      "
    or lboard == "      ?  " or lboard == "        ?"
    or lboard == " ?       " or lboard == "   ?     "
    or lboard == "     ?   " or lboard == "       ? "):

        pointer = 4

    if(lboard == "    ?    "):

        pointer = 0

    if(lboard[0] == '?'):

        if(lboard[2] == '?' and lboard[1] == ' '):

            pointer = 1

        if(lboard[6] == '?' and lboard[3] == ' '):

            pointer = 3

        if(lboard[8] == '?' and lboard[4] == ' '):

            pointer = 4

        if(lboard[1] == '?' and lboard[2] == ' '):

            pointer = 2

        if(lboard[3] == '?' and lboard[6] == ' '):

            pointer = 6

        if(lboard[4] == '?' and lboard[8] == ' '):

            pointer = 8

    newBoard = board[:pointer] + mark + board[pointer+1:]

    return newBoard

#Function for choosing whether the player wants to be X or O

def inputPlayerLetter():

    letter = ""

    while not(letter == 'X' or letter == "O"):
        letter = input("Do you want to be X or O? (X moves first) ").upper()

    if letter == "X":
        return(["X","O"])

    else:
        return(["O","X"])

#Function that checks whether the game is over
#(either player gets three in a row)

def checkWin(board):

    if(board[0] == board[1] == board[2] != " "
    or board[0] == board[3] == board[6] != " "
    or board[0] == board[4] == board[8] != " "):

        return(board[0] + " wins!")

    elif(board[6] == board[7] == board[8] != " "
    or board[6] == board[4] == board[2] != " "):

        return(board[6] + " wins!")

    elif(board[2] == board[5] == board[8] != " "):

        return(board[2] + " wins!")

    elif(not(" " in board)):

        return("Draw")

    else:

        return("Continue")

print("Welcome to Tic-Tac-Toe! \n")

#Main

while True:

    board = "         "

    p, c = inputPlayerLetter()
    print("Player character:", p)

    print("\nEntering moves: Enter the number of the box where you wish to place your move")
    print("The boxes are numbered as follows:")
    render("123456789")

    endState = "Game"
    movesPassed = 0

    while(endState == "Game"):

        if(movesPassed%2 == 0):

            if(p == "X"):

                board = userInput(board, p)
                print("\nYou have moved")

            else:

                board = computerInput(board, c)
                print("\nComputer has moved")

        else:

            if(p == "X"):

                board = computerInput(board, c)
                print("\nComputer has moved")

            else:

                board = userInput(board, p)
                print("\nYou have moved")

        render(board)
        movesPassed += 1

        if(checkWin(board) != "Continue"):

            print("\n"+checkWin(board))
            endState = "gameOver"

        else:

            pass

    contVar = ''

    while not(contVar == "Y" or contVar == "N"):

        contVar = input("\nDo you want to continue?(y/n)").upper().strip()

    if(contVar == "N"):

        break
