import random

def drawboard(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def isspacefree(board, move):
    return board[move] == ' '

def getplayermove(board):
    while True:
        move = input("What is your next move? (1-9): ").strip()
        if move.isdigit() and int(move) in range(1, 10) and isspacefree(board, int(move)):
            return int(move)
        print("Invalid move. Please choose an open space between 1 and 9.")

def inputplayerletter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be letter X or O?')
        letter = input().upper()
    return ['X', 'O'] if letter == 'X' else ['O', 'X']

def whogoesfirst():
    return 'computer' if random.randint(0, 1) == 0 else 'player'

def playagain():
    print('Do you want to play again? (yes or no)')
    return input().strip().lower().startswith('y')

def makemove(board, letter, move):
    board[move] = letter

def iswinner(bo, le):
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[7] == le and bo[4] == le and bo[1] == le) or
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[9] == le and bo[5] == le and bo[3] == le) or
        (bo[7] == le and bo[5] == le and bo[3] == le) or
        (bo[9] == le and bo[5] == le and bo[1] == le)
    )

def getboardcopy(board):
    return board[:]

def chooserandommovefromlist(board, moveList):
    possibleMoves = [move for move in moveList if isspacefree(board, move)]
    return random.choice(possibleMoves) if possibleMoves else None

def getcomputermove(theboard, computerletter):
    playerletter = 'O' if computerletter == 'X' else 'X'

    for i in range(1, 10):
        copy = getboardcopy(theboard)
        if isspacefree(copy, i):
            makemove(copy, computerletter, i)
            if iswinner(copy, computerletter):
                return i

    for i in range(1, 10):
        copy = getboardcopy(theboard)
        if isspacefree(copy, i):
            makemove(copy, playerletter, i)
            if iswinner(copy, playerletter):
                return i

    move = chooserandommovefromlist(theboard, [1, 3, 7, 9])
    if move is not None:
        return move

    if isspacefree(theboard, 5):
        return 5

    return chooserandommovefromlist(theboard, [2, 4, 6, 8])

def isboardfull(board):
    return all(not isspacefree(board, i) for i in range(1, 10))

print("Welcome to Tic Tac Toe!")

while True:
    theboard = [' '] * 10
    playerletter, computerletter = inputplayerletter()
    turn = whogoesfirst()
    print("The " + turn + " will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawboard(theboard)
            move = getplayermove(theboard)
            makemove(theboard, playerletter, move)

            if iswinner(theboard, playerletter):
                drawboard(theboard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False
            elif isboardfull(theboard):
                drawboard(theboard)
                print("The game is a tie!")
                break
            else:
                turn = 'computer'
        else:
            move = getcomputermove(theboard, computerletter)
            makemove(theboard, computerletter, move)

            if iswinner(theboard, computerletter):
                drawboard(theboard)
                print("The computer has beaten you! You lose.")
                gameIsPlaying = False
            elif isboardfull(theboard):
                drawboard(theboard)
                print("The game is a tie!")
                break
            else:
                turn = 'player'

    if not playagain():
        break