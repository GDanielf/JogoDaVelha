from IPython.display import clear_output
import random
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#functin to display the board
def display_board(board):
#   board = [ 0   1   2   3   4   5   6   7   8   9]
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    checkboard = []
    clear_output()
    for i in board:
        if i.lower()in 'xo':
            checkboard.append(i.upper())
        else:
            checkboard.append(' ')
    for i in range(1,len(checkboard)):
        board[i]=checkboard[i]
    print(' |   |   |   |\n | {} | {} | {} |\n |   |   |   |\n---------------\n |   |   |   |\n | {} | {} | {} |\n |   |   |   |\n---------------\n |   |   |   |\n | {} | {} | {} |\n |   |   |   |'.format(board[7],board[8],board[9],board[4],board[5],board[6],board[1],board[2],board[3]))
#Function to put the desired marker
    
def player_input():
    player = input("Please pick a marker 'X' or 'O'")
    while player.lower() not in 'xo':
        player = input("Please pick a marker 'X' or 'O'")
    player=player.upper()
    return player
#Function theat puts ther marker in the position
def place_marker(board, marker, position):
    board = [' ']
    x=0
    while x<=position:
        board.append(' ')
        x+=1
    board[x-1]=marker
    return display_board(board)
    

def win_check(board, mark):
    wincond = {'cond1':board[1]==mark and board[2]==mark and board[3]==mark,
              'cond2':board[4]==mark and board[5]==mark and board[6]==mark,
              'cond3':board[7]==mark and board[8]==mark and board[9]==mark,
              'cond4':board[7]==mark and board[5]==mark and board[3]==mark,
              'cond5':board[1]==mark and board[5]==mark and board[9]==mark,
              'cond6':board[1]==mark and board[4]==mark and board[7]==mark,
              'cond7':board[2]==mark and board[5]==mark and board[8]==mark,
              'cond8':board[3]==mark and board[6]==mark and board[9]==mark}
    return True in wincond.values()
def choose_first():
    x = random.randint(1,2)
    print(f'The player {x} goes first')
    return x
def space_check(board, position):
    return ' ' in board[position]
def full_board_check(board):
    return ' ' in board
def player_choice(board):
    position = int(input('Please enter a number 1-9: '))    
    while position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input('Please enter a integer number 1-9: '))
    if space_check(board,position):
        return position
    else:
        print('Position not available')
def replay():
    response = input("Do you want to play again: (y/n)")
    response.lower()
    while response!='y' or response!='n':
        response = input("Do you want to play again: (y/n)")
    return response=='y'


#test
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
choose_first()
display_board(board)
Markplayer = ''
MarkPlayer1 = player_input()
if MarkPlayer1 =='X': MarkPlayer2='O'
else: MarkPlayer2=='X'
#Player 1 Turn
print(f'Player No 1 time to play.')
player_choice(board)
while player_choice(board) not in [1,2,3,4,5,6,7,8,9]:
    player_choice(board) 
place_marker(board,MarkPlayer1,player_choice(board))
display_board(board)
# Player2's turn.
print(f'Player No 2 time to play.')
player_choice(board)
while player_choice(board) not in [1,2,3,4,5,6,7,8,9]:
    player_choice(board) 
place_marker(board,MarkPlayer1,player_choice(board))
display_board(board)