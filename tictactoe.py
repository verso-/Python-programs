#Sam Verma
#tic tac toe
#user picks X or O and then plays against the computer

import random

def drawBoard(board):
    #prints out the board

    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])

def inputUserLetter():
    #user types what letter they want to be
    #return list with user letter as first item and comp letter as second
    letter=''
    while not(letter=='X' or letter=='O'):
        print('Do you want to be X or O?')
        letter=input().upper()

    if letter=='X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    #randomly chooses user who goes first
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'user'

def playAgain():
    #returns True if the user wants to user again, False otherwise
    print('Play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move]=letter

def isWinner(bo,le):
    #given a board and a user's letter, returns True if that user has won
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[4]==le and bo[5]==le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[7]==le and bo[4]==le and bo[1]==le) or
            (bo[8]==le and bo[5]==le and bo[2]==le) or
            (bo[9]==le and bo[6]==le and bo[3]==le) or
            (bo[7]==le and bo[5]==le and bo[3]==le) or
            (bo[9]==le and bo[5]==le and bo[1]==le))

def getBoardCopy(board):
    #copy board and return that
    copy=[]

    for i in board:
        copy.append(i)

    return copy

def isSpaceFree(board, move):
    #return true if passed move is free
    return board[move]==''

def getUserMove(board):
    #user types in move
    move=''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('Next move? (1-9)')
        move=input()
    return int(move)

def chooseRandMoveFromList(board,movesList):
    #returns valid move from passed list on passed board
    #returns none if no valid move
    possibleMoves=[]
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None

def getCompMove(board,compLetter):
    #given board and comp's letter, determine move and return it
    if compLetter=='X':
        userLetter='O'
    else:
        userLetter='X'

    #AI algorithm. First check if next move wins
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,compLetter,i)
            if isWinner(copy,compLetter):
                return i        

    #check if user could win on next move and block it
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,userLetter,i)
            if isWinner(copy,userLetter):
                return i

    #try to take one of the corners if they are free
    move=chooseRandMoveFromList(board,[1,3,7,9])
    if move!=None:
        return move

    #try to take center
    if isSpaceFree(board,5):
        return 5

    #move on one of the sides
    return chooseRandMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    #return True if every space taken
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

print('Welcome to Tic Tac Toe')

while True:
    #reset the board
    game = ['']*10
    userLetter,compLetter=inputUserLetter()
    turn=whoGoesFirst()
    print('The '+turn+' will go first')
    gameIsOn=True

    while gameIsOn:
        if turn=='user':
            #user's turn
            drawBoard(game)
            move=getUserMove(game)
            makeMove(game,userLetter,move)

            if isWinner(game,userLetter):
                drawBoard(game)
                print('Winner! You have won!')
                gameIsOn=False
            else:
                if isBoardFull(game):
                    drawBoard(game)
                    print('Tie! No winner!')
                    break
                else:
                    turn='computer'

        else:
            #computer's turn
            move=getCompMove(game,compLetter)
            makeMove(game,compLetter,move)

            if isWinner(game,compLetter):
                drawBoard(game)
                print('Loser! The computer has won!')
                gameIsOn=False
            else:
                if isBoardFull(game):
                    drawBoard(game)
                    print('Tie! No winner!')
                    break
                else:
                    turn='user'

    if not playAgain():
        break
                

    
