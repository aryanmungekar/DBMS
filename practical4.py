def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    # Base case: if all queens are placed, return True
    if col >= n:
        return True

    # Consider this column and try placing a queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col] (backtrack)
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False


def print_board(board, n):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))


def n_queens():
    n = int(input("Enter the number of queens (N): "))
    board = [[0] * n for _ in range(n)]
    if solve_n_queens(board, 0, n):
        print("Solution for", n, "Queens:")
        print_board(board, n)
    else:
        print("No solution exists for", n, "Queens.")


# Run the n_queens function to start
n_queens()

#The n_queens function begins by prompting the user to input the number of queens (n). 
#The input is stored as an integer, which will be the number of queens and also 
#the dimension of the chessboard (an n x n board).
#We initialize a board represented by a 2D list of zeros. Each element in this n x n list is set to 0, meaning no queen is placed there initially.
#Each row represents a row on the chessboard, and each element in a row (column) can either be 0 (empty) or 1 (contains a queen).
#The solve_n_queens function is designed to try placing queens column by column, from the first column (leftmost) to the last (rightmost).
#To ensure no two queens threaten each other, is_safe checks three conditions:
#Row Check: It verifies that no queens are already placed in the same row on the left side.
#Upper Left Diagonal Check: It ensures that no queens are on the upper left diagonal.
#Lower Left Diagonal Check: It checks the lower left diagonal for any existing queens.
#If a queen is placed such that none of these conditions are violated, it’s considered a safe position.
#If a safe position is found, the queen is placed there (the cell is set to 1).
#The function then recursively attempts to place queens in the next column.

