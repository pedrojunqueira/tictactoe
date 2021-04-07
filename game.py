import os

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

def init_game():
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    return [], [], board

players_symbol = ["X", "O"]
players, turn_player, board =  init_game()

grid_map = {"A": (0,0), "B":(0,1), "C":(0,2),
        "D": (1,0), "E":(1,1), "F":(1,2),
        "G":(2,0), "H":(2,1), "I":(2,2)}

grid_legend = [["A","B","C"],["D","E","F"],["G","H","I"]]

def chose_players():
    turn = None
    if len(players) < 2:
        name = input(f"Player{len(players)+1} what is your name?\n")
        players.append(Player(name=name, symbol=players_symbol[len(players)]))


def print_board(board):
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            print(f" |{item}| ", end="")
            if j==2:
                print("\n")


def play(player, coordinate):
    if str(coordinate).upper() not in grid_map.keys():
        print("This position is not valid, chose another")
        return 0
    row, column = grid_map[coordinate.upper()]
    if board[row][column] == " ":
        board[row][column] = player.symbol
        return 1
    else:
        print("This position already taken or not valid, chose another")
        return 0


def find_winner(board):
    #find row winner
    rows = [set(row) for row in board]

    for row in rows:
        if len(row) ==1 and list(row)[0] !=' ':
            return list(row)[0]

    #find column winner
    cols = [set([row[i] for row in board]) for i in range(3)]
    for col in cols:
        if len(col) == 1 and list(col)[0] != ' ':
            return list(col)[0]
        
    # find diagonal winner
    diag1 = set([ board[i][i] for i in range(3)])
    diag2 = set([ board[i][j] for i, j in zip(range(3),sorted(list(range(3)),reverse=True))])
    for diag in [diag1,diag2]:
        if len(diag) == 1 and list(diag)[0] != ' ':
            return list(diag)[0]
    return 0


while True:
    if len(players) < 2:
    os.system('clear')
    print("\n")
    print("Options")
    print("(C)hoose Players")
    print("(S)tart Game")
    print("(R)eset Game")
    print("(E)xit")
    print("\n")
    option = input("Chose option \n").upper()
    if option == "C":
        if len(players) < 2:
            chose_players()
        else:
            print(f"Player(s) {' and '.join([ player.name for player in players])} already chosen to start game chose (S)") 
            continue
    if option == "S":
        if option in ["R", "E"]:
            break
        if len(players) < 2:
            print("""Need 2 player to start game

            """)
            continue
        turn_player = [players[0]]
        while True:
            print_board(board)
            active_player = [player for player in players if player in turn_player][0]
            print(f"{active_player.name} is playing")
            print(f"\n")
            print_board(grid_legend)
            coordinate = input("Chose a coordinate\n")
            validate_round = play(active_player, coordinate)
            while not validate_round:
                coordinate = input("Chose a coordinate\n")
                validate_round = play(active_player, coordinate)
                if validate_round:
                    break
            winner = find_winner(board)
            if winner:
                winner_name = [player.name for player in players if player.symbol == winner][0]
                print(f"the winner is: {winner_name}")
                print("\n")
                print_board(board)
                option = input("Would like to (R)estart or (E)xit \n").upper()
                break
            turn_player = [player for player in players if player not in turn_player]

    if option == "R":
        print("reseting game")
        players, turn_player, board =  init_game()
        continue

    if option == "E":
        break
