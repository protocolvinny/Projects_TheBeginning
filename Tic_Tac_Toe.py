'''
My first game ever - Tic Tac Toe!!!

Be Warned: This was created in Jupyter
'''

from IPython.display import clear_output

#Create and display a board
def display_board(board):
    clear_output() #Clears old versions of the board each time it's printed
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])

test_board = [' '] * 10
display_board(test_board)

#Allow player input to get the game started
def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = '' #Marker starts off blank
    # KEEP ASKING PLAYER 1 TO CHOOSE X OR O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    # ASSIGN PLAYER 2 THE OPPOSITE MARKER
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#Places input at assigned positions on the board
def place_marker(board, marker, position):
    board[position] = marker

#Check for a winner
def win_check(board, mark):
    #Check ROWS
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    #Check COLUMNS
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    #Check DIAGONALS
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

#Randomly decide which player goes first
import random
def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
#Checks board for free spaces/empty string
def space_check(board, position):
    
    return board[position] == ' '
    
#Checks to see if the board is full
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full if we return True
    return True

def player_choice(board):
    
    position = 0
    #Checks to see if player provides valid input or chooses an already filled space
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    
    return position

def replay():
    
    choice = input('Play again? Enter Yes or No')
    return choice == 'Yes'

#While loop to keep running the game
print('Welcome to TIC TAC TOE')

while True:
    
    #Play the game
    
    #Set everything up (board, who's first, choose markers x,o)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Ready to play? y or n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    #Game play
    while game_on:
        if turn == 'Player 1':
            #Show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Check if they won
            place_marker(the_board,player1_marker,position)
            #Or check if there is a tie
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            #Show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            #Check if they won
            place_marker(the_board,player2_marker,position)
            #Or check if there is a tie
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
    

    #Break out of the while loop on replay()
    if not replay():
        break
