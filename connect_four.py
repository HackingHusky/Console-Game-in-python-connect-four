ROWS = 6
COLUMNS = 7

# Create the board for the game
def create_board():
    board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
    return board
# print the board 
def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        #drop pieces into the board
def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = piece
            return True
    return False
        # look for the winner 
def is_winner(board, piece):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == piece:
                return True
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == piece:
                return True
    # Check diagonal (positive slope)
    for col in range(COLUMNS - 3):
        for row in range(ROWS - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == piece:
                return True
    # Check diagonal (negative slope)
    for col in range(COLUMNS - 3):
        for row in range(3, ROWS):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == piece:
                return True
    return False
        # add draw if game goes into a draw
def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))
        # playing the game
def play_game():
    board = create_board()
    current_piece = 'X'
    while True:
        print_board(board)
        column = int(input(f"Player {current_piece}, choose a column (0-{COLUMNS-1}): "))
        if column < 0 or column >= COLUMNS or not drop_piece(board, column, current_piece):
            print("Invalid move. Try again.")
            continue
        if is_winner(board, current_piece):
            print_board(board)
            print(f"Player {current_piece} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_piece = 'O' if current_piece == 'X' else 'X'
        #don't for get to ask to play again with the end user
        play_again = input("Wanna play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
   