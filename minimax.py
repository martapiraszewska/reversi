import math
from heuristic import heuristic
from reversi import get_possible_moves, is_gameover, get_winner, make_move


def minimax(state, depth, alpha, beta, ai_player):
    board, curr_player = state
    if is_gameover(state):
        winner = get_winner(board)
        if winner == ai_player:
            return 10000
        return -10000
    if depth == 0:
        return heuristic(board, ai_player)

    moves = get_possible_moves(state)
    opponent = 'o' if curr_player == 'x' else 'x'

    if len(moves) == 0:
        new_state = (board, opponent)
        return minimax(new_state, depth - 1, alpha, beta, ai_player)

    if curr_player == ai_player:
        max_eval = -math.inf
        max_eval = get_max_eval(state, moves, max_eval, depth, alpha, beta, ai_player)
        return max_eval

    else:
        min_eval = math.inf
        min_eval = get_min_eval(state, moves, min_eval, depth, alpha, beta, ai_player)
        return min_eval


def get_max_eval(state, moves, max_eval, depth, alpha, beta, ai_player):
    _ , curr_player = state
    if len(moves) == 0:
        return max_eval
    new_curr_player = 'o' if curr_player == 'x' else 'x'
    new_board = make_move(state, moves[0])
    new_state = (new_board, new_curr_player)
    eval = minimax(new_state, depth - 1, alpha, beta, ai_player)
    max_eval = max(max_eval, eval)
    alpha = max(alpha, eval)
    if beta <= alpha:
        return max_eval
    return get_max_eval(state, moves[1:], max_eval, depth, alpha, beta, ai_player)


def get_min_eval(state, moves, min_eval, depth, alpha, beta, ai_player):
    _ , curr_player = state
    if len(moves) == 0:
        return min_eval
    new_curr_player = 'w' if curr_player == 'b' else 'b'
    new_board = make_move(state, moves[0])
    new_state = (new_board, new_curr_player)
    eval = minimax(new_state, depth - 1, alpha, beta, ai_player)
    min_eval = min(min_eval, eval)
    beta = min(beta, eval)
    if beta <= alpha:
        return min_eval
    return get_min_eval(state, moves[1:], min_eval, depth, alpha, beta, ai_player)


def get_best_move(state, depth):
    moves = get_possible_moves(state)

    return choose_move(state, moves, depth, None, -math.inf)


def choose_move(state, moves, depth, best_move, best_eval):
    if len(moves) == 0:
        return best_move

    move = moves[0]
    _, curr_player = state
    opponent = 'o' if curr_player == 'x' else 'x'
    new_board = make_move(state, move)
    new_state = (new_board, opponent)
    value = minimax(new_state, depth - 1, -math.inf, math.inf, curr_player)

    if value > best_eval:
        best_eval = value
        best_move = move

    return choose_move(state, moves[1:], depth, best_move, best_eval)
