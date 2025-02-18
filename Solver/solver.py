# 0 : means empty cell
# 1 : could be X or O it doesnt matter it mean player 1 place symbol on that cell
# 2 : could be X or O it doesnt matter it mean player 2 place symbol on that cell



# Create Empty Board
def create_empty_board():
    board = [[0, 0, 0], 
             [0, 0, 0], 
             [0, 0, 0]]
    return board



# Print Board 
def print_board(board):
    for row in board:
        print(row)



# Is Board Full
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True



# Find Winner
def find_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return "Player 1 win by row match" if board[i][0] == 1 else "Player 2 win by row match"
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return "Player 1 win by column match" if board[0][i] == 1 else "Player 2 win by column match"
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return "Player 1 win by diagonal match" if board[0][0] == 1 else "Player 2 win by diagonal match"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return "Player 1 win by diagonal match" if board[0][2] == 1 else "Player 2 win by diagonal match"
    if is_board_full(board):
        return "Match is draw"
    return "Match is still on going"



# Fill Board
def fill_board(board, position, player):
    if position == 1:
        board[0][0] = player
    elif position == 2:
        board[0][1] = player
    elif position == 3:
        board[0][2] = player
    elif position == 4:
        board[1][0] = player
    elif position == 5:
        board[1][1] = player
    elif position == 6:
        board[1][2] = player
    elif position == 7:
        board[2][0] = player
    elif position == 8:
        board[2][1] = player
    elif position == 9:
        board[2][2] = player

    return board



# Generate all possible moves
class TreeNode9Branch:
    def __init__(self, board, player=None, move=None):
        self.board = board 
        self.player = player
        self.move = move

        self.first = None
        self.second = None
        self.third = None
        self.fourth = None
        self.fifth = None
        self.sixth = None
        self.seventh = None
        self.eighth = None
        self.ninth = None

        self.player1_wins = 0
        self.player2_wins = 0
        self.draws = 0

    def set_child(self, position, child):
        if position == 1:
            self.first = child
        elif position == 2:
            self.second = child
        elif position == 3:
            self.third = child
        elif position == 4:
            self.fourth = child
        elif position == 5:
            self.fifth = child
        elif position == 6:
            self.sixth = child
        elif position == 7:
            self.seventh = child
        elif position == 8:
            self.eighth = child
        elif position == 9:
            self.ninth = child

def print_all_children(root):
    for i in range(1, 10):
        child = getattr(root, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth'][i-1]}")
        if child:
            print("--------------------------------------------------")
            print(f"Fill cell {child.move} by Player-{child.player}:")
            print_board(child.board)
            print(f"Player 1 Wins: {child.player1_wins}")
            print(f"Player 2 Wins: {child.player2_wins}")
            print(f"Draws: {child.draws}")
            print("--------------------------------------------------")

def generate_all_possible_moves(root, player):
    winner = find_winner(root.board)

    if winner == "Player 1 win by row match" or winner == "Player 1 win by column match" or winner == "Player 1 win by diagonal match":
        root.player1_wins = 1
        return root.player1_wins, root.player2_wins, root.draws
    elif winner == "Player 2 win by row match" or winner == "Player 2 win by column match" or winner == "Player 2 win by diagonal match":
        root.player2_wins = 1
        return root.player1_wins, root.player2_wins, root.draws
    elif winner == "Match is draw":
        root.draws = 1
        return root.player1_wins, root.player2_wins, root.draws

    for i in range(1, 10):  
        row, col = divmod(i - 1, 3)
        if root.board[row][col] == 0:  
            new_board = [r[:] for r in root.board] 
            new_board[row][col] = player  

            new_node = TreeNode9Branch(new_board, player, i)
            root.set_child(i, new_node)  
            
            p1_wins, p2_wins, draws = generate_all_possible_moves(new_node, 3 - player)

            root.player1_wins += p1_wins
            root.player2_wins += p2_wins
            root.draws += draws

    return root.player1_wins, root.player2_wins, root.draws

def calculate_and_print_rates(root):
    total_sample_space = root.player1_wins + root.player2_wins + root.draws
    if total_sample_space == 0:
        print("No games in the sample space.")
        return

    player1_win_rate = (root.player1_wins / total_sample_space) * 100
    player2_win_rate = (root.player2_wins / total_sample_space) * 100
    draw_rate = (root.draws / total_sample_space) * 100

    print(f"Player 1 Win Rate: {player1_win_rate:.2f}%")
    print(f"Player 2 Win Rate: {player2_win_rate:.2f}%")
    print(f"Draw Rate: {draw_rate:.2f}%")



root = TreeNode9Branch(create_empty_board())
generate_all_possible_moves(root, 1)
print()
print("All moves generated")



# Input Handle
print()
inp = input("Enter cell filling history : ").split(",")
print()
cell_fill_history = list(map(int, inp))  



# Fill board 
board = create_empty_board()
for i in range(len(cell_fill_history)):
    fill_board(board, cell_fill_history[i], 1 if i % 2 == 0 else 2)
print()
print()
print()
print("Current Board :")
print_board(board)
print()
print()
print()
print()



# Traverse the tree
new_root = root
for i in cell_fill_history:
    child = getattr(new_root, f"{['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth'][i-1]}")
    new_root = child
print("--------------------------------------------------")
print_all_children(new_root)
print("--------------------------------------------------")
calculate_and_print_rates(new_root)

cell_fill_history.append(5)
# Second Player Place in the corner
cell_fill_history.append(1)
# First Player Place at the edge near second player corner
cell_fill_history.append(2)
# And so on
cell_fill_history.append(8)
cell_fill_history.append(7)
cell_fill_history.append(3)
cell_fill_history.append(4)
cell_fill_history.append(6)
cell_fill_history.append(9)

# Example Test Cases
# Enter cell filling history : 5, 2, 9, 3
# Enter cell filling history : 5                           (First Player start at the middle cell)
# Enter cell filling history : 5, 1, 2, 8, 7, 3, 4, 6, 9   (Perfectly executed game)