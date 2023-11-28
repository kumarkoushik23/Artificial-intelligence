def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, col):
    if col >= len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1):
                return True
            board[i][col] = 0

    return False

def solve_nqueens():
    n = 8  # You can change this to solve for other board sizes
    board = [[0] * n for _ in range(n)]

    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")
        return

    print("Solution:")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    solve_nqueens()
