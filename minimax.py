import math
from heuristic import heuristic
from reversi import get_possible_moves, is_gameover, get_winner, make_move


def evaluation(board, ai_player):
    # opponent = 'w' if ai_player == 'b' else 'b'
    # return heuristic(board, ai_player) - heuristic(board, opponent)
    return heuristic(board, ai_player)


def minimax(curr_board, depth, alpha, beta, current_player, ai_player):
    if is_gameover(curr_board, current_player):
        winner = get_winner(curr_board)
        if winner == ai_player:
            return 10000
        return -10000
    if depth == 0:
        return evaluation(curr_board, ai_player)

    moves = get_possible_moves(curr_board, current_player)
    if current_player == ai_player:
        max_eval = -math.inf
        max_eval = get_max_eval(curr_board, moves, max_eval, depth, alpha, beta, current_player, ai_player)
        return max_eval

    else:
        min_eval = math.inf
        min_eval = get_min_eval(curr_board, moves, min_eval, depth, alpha, beta, current_player, ai_player)
        return min_eval


def get_max_eval(curr_board, moves, max_eval, depth, alpha, beta, current_player, ai_player):
    if len(moves) == 0:
        return max_eval
    new_curr_player = 'w' if current_player == 'b' else 'b'
    new_board = make_move(curr_board, moves[0], current_player)
    eval = minimax(new_board, depth - 1, alpha, beta, new_curr_player, ai_player)
    max_eval = max(max_eval, eval)
    alpha = max(alpha, eval)
    if beta <= alpha:
        return max_eval
    return get_max_eval(curr_board, moves[1:], max_eval, depth, alpha, beta, current_player, ai_player)


def get_min_eval(curr_board, moves, min_eval, depth, alpha, beta, current_player, ai_player):
    if len(moves) == 0:
        return min_eval
    new_curr_player = 'w' if current_player == 'b' else 'b'
    new_board = make_move(curr_board, moves[0], current_player)
    eval = minimax(new_board, depth - 1, alpha, beta, new_curr_player, ai_player)
    min_eval = min(min_eval, eval)
    beta = min(beta, eval)
    if beta <= alpha:
        return min_eval
    return get_min_eval(curr_board, moves[1:], min_eval, depth, alpha, beta, current_player, ai_player)
    

if __name__ == '__main__':
    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'w', 'e', 'w', 'e'],
        ['e', 'e', 'e', 'b', 'w', 'w', 'e', 'e'],
        ['e', 'e', 'e', 'b', 'b', 'b', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'w', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]
    val = minimax(board, 10, -math.inf, math.inf, 'b', 'b')
    print(val)