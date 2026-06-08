import random
from reversi import (
    get_possible_moves,
    get_start_state,
    update_state,
    is_gameover,
    get_winner
)
from minimax import get_best_move


def random_move(state):
    moves = get_possible_moves(state)

    if len(moves) == 0:
        return None

    return random.choice(moves)


def play_minimax_vs_random(state, depth, ai_player):
    board, current_player = state

    if is_gameover(state):
        return get_winner(board)

    if current_player == ai_player:
        move = get_best_move(state, depth)
    else:
        move = random_move(state)

    new_state = update_state(state, move)
    return play_minimax_vs_random(new_state, depth, ai_player)


def simulate_games(depth, games, ai_player, wins=0, draws=0, losses=0):
    if games == 0:
        return wins, draws, losses

    winner = play_minimax_vs_random(get_start_state(), depth, ai_player)

    if winner is None:
        return simulate_games(depth, games - 1, ai_player, wins, draws + 1, losses)

    ai_won = (winner == ai_player)

    if ai_won:
        return simulate_games(depth, games - 1, ai_player, wins + 1, draws, losses)

    return simulate_games(depth, games - 1, ai_player, wins, draws, losses + 1)
