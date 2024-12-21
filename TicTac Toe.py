# Function to print the Tic Tac Toe board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")


# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


# Function to check if the board is full (for a draw)
def check_draw(board):
    return all(cell != " " for row in board for cell in row)


# Function to handle player input and make a move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell is already occupied! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")


# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize empty board
    current_player = "X"  # Player X starts the game

    print_board(board)

    while True:
        player_move(board, current_player)  # Take player input and make move
        print_board(board)  # Print the updated board

        if check_win(board, current_player):  # Check if the current player wins
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):  # Check if the game is a draw
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"  # Switch player


# Start the game
if __name__ == "__main__":
    tic_tac_toe()
