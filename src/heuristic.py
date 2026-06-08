WEIGHTS = [
    [100, -20, 10,  5,  5, 10, -20, 100],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [10,   -2, -1, -1, -1, -1,  -2,  10],
    [5,    -2, -1, -1, -1, -1,  -2,   5],
    [5,    -2, -1, -1, -1, -1,  -2,   5],
    [10,   -2, -1, -1, -1, -1,  -2,  10],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [100, -20, 10,  5,  5, 10, -20, 100]
]


def get_weight(i, j, color, player):
    if color == ' ':
        return 0
    if color == player:
        return WEIGHTS[i][j]
    return -WEIGHTS[i][j]

def heuristic(board, player):
    score = sum(get_weight(i, j, col, player) for i, row in enumerate(board) for j, col in enumerate(row))
    return score
