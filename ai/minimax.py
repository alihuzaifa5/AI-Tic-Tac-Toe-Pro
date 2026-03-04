def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            return 10 if board[row][0] == 'O' else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return 10 if board[0][col] == 'O' else -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return 10 if board[0][0] == 'O' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return 10 if board[0][2] == 'O' else -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10: return score - depth
    if score == -10: return score + depth
    if not any("" in row for row in board): return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ""
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ""
        return best

def find_best_move(board):
    best_val = -1000
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = ""
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move