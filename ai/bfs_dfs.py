from collections import deque
from ai.minimax import check_winner, available_moves


# -------------------------
# BFS: Can AI reach a win?
# -------------------------
def bfs_can_win(board):
    queue = deque()
    queue.append(board.copy())

    while queue:
        current = queue.popleft()
        if check_winner(current) == "O":
            return True

        for move in available_moves(current):
            new_board = current.copy()
            new_board[move] = "O"
            queue.append(new_board)

    return False


# -------------------------
# DFS: Explore all outcomes
# -------------------------
def dfs_outcomes(board):
    result = check_winner(board)
    if result:
        return {result: 1}

    outcomes = {"X": 0, "O": 0, "Draw": 0}

    for move in available_moves(board):
        new_board = board.copy()
        new_board[move] = "O"
        sub_result = dfs_outcomes(new_board)

        for key in outcomes:
            outcomes[key] += sub_result.get(key, 0)

    return outcomes