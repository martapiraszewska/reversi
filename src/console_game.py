from reversi import get_possible_moves, get_start_state, update_state, get_winner, is_gameover
from minimax import get_best_move
import math


def print_board(board):
    print("    a   b   c   d   e   f   g   h")
    print("  |————————————————————————————————")
    for i, row in enumerate(board):
        print(f"{i + 1} |", end='')
        for j, piece in enumerate(row):
            if j == 7:
                print(f" {piece} |")
            else:
                print(f" {piece} |", end='')
        print("  |————————————————————————————————")


def convert_from_human_move(move):
    if len(move) != 2:
        return None
    x = move[0]
    if not x.isdigit():
        return None
    converted_x = int(x) - 1
    y = move[1]
    if y not in "abcdefgh":
        return None
    converted_y = ord(y) - 97
    return (converted_x, converted_y)


def convert_to_human_move(move):
    x, y = move
    converted_y = chr(y + ord('a'))
    converted_move = str(x + 1) + converted_y
    return converted_move


def print_game_over(winner):
    print("-" * 40)
    print("Game over!")
    if winner is None:
        print("Draw")
    else:
        print(f'{winner} wins!')
    print("-" * 40)


def print_possible_moves(possible_moves):
    print("Possible moves: ", end='')
    for move in possible_moves:
        converted_move = convert_to_human_move(move)
        print(f"{converted_move}, ", end='')
    print('\n')


def print_menu():
    print("Game options:")
    print("1. player vs player")
    print("2. player vs ai (easy)")
    print("3. player vs ai (medium)")
    print("4. player vs ai (hard)")
    print("5. Exit")


def print_turn(player):
    print()
    print("-" * 40)
    print(f"Current player: {player}")


def print_ai_move(move):
    print(f"AI played {convert_to_human_move(move)}")


def print_pass(player):
    print(f"{player} has no legal moves and must pass.")


def get_game_option():
    game_option = input("Choose option (1-5): ")
    return game_option


def human_player(state):
    possible_moves = get_possible_moves(state)
    print_possible_moves(possible_moves)
    move = move_input_loop(possible_moves)
    return move


def ai_player_easy(state):
    best_move = get_best_move(state, 2)
    print_ai_move(best_move)
    return best_move  


def ai_player_medium(state):
    best_move = get_best_move(state, 3)
    print_ai_move(best_move)
    return best_move


def ai_player_hard(state):
    best_move = get_best_move(state, 4)
    print_ai_move(best_move)
    return best_move


def main_loop(state, players):
    board, curr_player = state
    print_turn(curr_player)
    print_board(board)
    if is_gameover(state):
        winner = get_winner(board)
        print_game_over(winner)
        return
    possible_moves = get_possible_moves(state)
    if len(possible_moves) == 0:
        print_pass(curr_player)
        move = None
    else:
        player_fn = players[0] if curr_player == 'x' else players[1]
        move = player_fn(state)
    state = update_state(state, move)
    return main_loop(state, players)


def move_input_loop(possible_moves):
    human_move = input("Make a move: ")
    move = convert_from_human_move(human_move)
    if move in possible_moves:
        return move
    print("Incorrect move, try again")
    return move_input_loop(possible_moves)


def game():
    print_menu()
    game_option = get_game_option()
    if game_option == "1":
        player_black = human_player
        player_white = human_player
    elif game_option == "2":
        player_black = human_player
        player_white = ai_player_easy
    elif game_option == "3":
        player_black = human_player
        player_white = ai_player_medium
    elif game_option == "4":
        player_black = human_player
        player_white = ai_player_hard
    else:
        return
    state = get_start_state()
    players = (player_black, player_white)
    main_loop(state, players)
