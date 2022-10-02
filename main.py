board = {1:'- - -',
         2:'- - -',
         3:'- - -'}
used_positions = []
gameOn = True
playerOneTurn = True

def change_player(player):
    global playerOneTurn
    playerOneTurn = not playerOneTurn

def draw_board():
    for i in board:
        print(board.get(i))

def check_if_game_over():
    global gameOn
    if (playerOneTurn):
        player = "Player 1"
    else:
        player = "Player 2"

    #check horizontals
    rowOne = list(board[1])
    if (rowOne[0] == rowOne[2] == rowOne[4]) and '-' not in rowOne:
        print(f"{player} wins")
        gameOn = False

    rowTwo = list(board[2])
    if (rowTwo[0] == rowTwo[2] == rowTwo[4]) and '-' not in rowTwo:
        print(f"{player} wins")
        gameOn = False

    rowThree = list(board[3])
    if (rowThree[0] == rowThree[2] == rowThree[4]) and '-' not in rowThree:
        print(f"{player} wins")
        gameOn = False

    #check verticals
    if (rowThree[0] == rowTwo[0] == rowOne[0]) and '-' not in rowThree[0]:
        print(f"{player} wins")
        gameOn = False

    if (rowThree[2] == rowTwo[2] == rowOne[2]) and '-' not in rowThree[2]:
        print(f"{player} wins")
        gameOn = False

    if (rowThree[4] == rowTwo[4] == rowOne[4]) and '-' not in rowThree[4]:
        print(f"{player} wins")
        gameOn = False

    #check diagonals
    if (rowOne[0] == rowTwo[2] == rowThree[4]) and '-' not in rowTwo[2]:
        print(f"{player} wins")
        gameOn = False

    if (rowOne[4] == rowTwo[2] == rowThree[0]) and '-' not in rowTwo[2]:
        print(f"{player} wins")
        gameOn = False

    #check if tie
    if not (rowOne.__contains__('-') or rowTwo.__contains__('-') or rowThree.__contains__('-')):
        print("This game is a tie")

def update_position(position, row, player):
    if position == 1 or position == 4 or position == 7:
        temp = list(board[row])
        temp[0] = player
        board[row] = "".join(temp)
    if position == 2 or position == 5 or position == 8:
        temp = list(board[row])
        temp[2] = player
        board[row] = "".join(temp)
    if position == 3 or position == 6 or position == 9:
        temp = list(board[row])
        temp[4] = player
        board[row] = "".join(temp)
    draw_board()
    check_if_game_over()
    change_player(playerOneTurn)

def select_position():
    if playerOneTurn:
        player = 'X'
        name = 'Player 1'
    else:
        player = 'O'
        name = 'Player 2'
    position_selection = int(input(f"{name}: Enter the position you wish to procure"))
    return position_selection, player

print("\nWelcome to Tic-Tac-Toe, use the keys 1-9 which are mapped like a telephone to the grid below")
draw_board()

while gameOn:
    position, player = select_position()
    while position in used_positions:
        position, player = select_position()
    used_positions.append(position)
    if position == 1 or position == 2 or position == 3:
        row = 1
    if position == 4 or position == 5 or position == 6:
        row = 2
    if position == 7 or position == 8 or position == 9:
        row = 3
    update_position(position, row, player)