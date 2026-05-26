def get_starting_piece(i, j):
    if (i == 3 and j == 3) or (i == 4 and j == 4):
        return 'b'
    elif (i == 3 and j == 4) or (i == 4 and j == 3):
        return 'w'
    return 'e'


def generate_start_board():
    rows, cols = 8, 8
    board = [[get_starting_piece(i, j) for j in range(cols)] for i in range(rows)]
    return board


def get_start_state():
    board = generate_start_board()
    curr_player = 'b'
    consecutive_passes = 0
    state = (board, curr_player, consecutive_passes)
    return state


def is_outside(cell):
    x, y = cell
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return True
    return False


def check_direction(board, cell, direction, player):
    next_cell = tuple(map(lambda x, y: x + y, cell, direction))
    if is_outside(next_cell):
        return None
    x, y = next_cell
    if board[x][y] == 'e':
        return None
    elif board[x][y] != player:
        end_cell = check_direction(board, next_cell, direction, player)
    else:
        return next_cell
    return end_cell


def map_sign(number):
    if number == 0:
        return 0
    if number < 0:
        return -1
    return 1


def get_flips_in_direction(direction, board, move_cell, player):
    end_cell = check_direction(board, move_cell, direction, player)
    if end_cell is not None:
        x, y = move_cell
        end_x, end_y = end_cell
        if abs(x - end_x) > 1 or abs(y - end_y) > 1:
            dx = map_sign(end_x - x)
            dy = map_sign(end_y - y)
            distance = max(abs(end_x - x), abs(end_y - y))
            pieces_to_flip = [(x + k * dx, y + k * dy) for k in range(1, distance)]
            return pieces_to_flip
    return []


def update_cell(pieces_to_flip, cell, cell_state, player):
    if cell not in pieces_to_flip:
        return cell_state
    if cell_state == 'e':
        return player
    elif cell_state == 'b':
        return 'w'
    return 'b'


def generate_new_board(board, pieces_to_flip, player):
    new_board = [
        [update_cell(pieces_to_flip, (i, j), col, player) for j, col in enumerate(row)] for i, row in enumerate(board)]
    return new_board


def make_move(board, move_cell, player):
    directions = [
        (-1, 0), (1, 0),    # up and down
        (0, -1), (0, 1),    # left and right
        (-1, -1), (-1, 1),   # diagonal
        (1, -1), (1, 1),
    ]
    pieces_to_flip = [get_flips_in_direction(direction, board, move_cell, player) for direction in directions]
    flatten_pieces = [piece for row in pieces_to_flip for piece in row]
    all_pieces_to_flip = set(flatten_pieces + [move_cell])
    new_board = generate_new_board(board, all_pieces_to_flip, player)
    return new_board


def check_move(board, move_cell, direction, player):
    x, y = move_cell
    end_cell = check_direction(board, move_cell, direction, player)
    if end_cell is not None:
        end_x, end_y = end_cell
        if abs(x - end_x) > 1 or abs(y - end_y) > 1:
            return move_cell
    return None


def get_possible_moves(board, player):
    empty_cells = [[(i, j) for j, col in enumerate(row) if col == 'e'] for i, row in enumerate(board)]
    empty_cells_flatten = [cell for row in empty_cells for cell in row]
    directions = [
        (-1, 0), (1, 0),    # up and down
        (0, -1), (0, 1),    # left and right
        (-1, -1), (-1, 1),   # diagonal
        (1, -1), (1, 1),
    ]
    moves = [
        check_move(board, cell, direction, player) for cell in empty_cells_flatten for direction in directions]
    moves_without_none = [move for move in moves if move is not None]
    moves_without_duplicates = list(set(moves_without_none))
    return moves_without_duplicates


def update_state(state, move):
    board, player, consecutive_passes = state
    new_player = 'b' if player == 'w' else 'w'
    if move is None:
        new_consecutive_passes = consecutive_passes + 1
    else:
        new_consecutive_passes = 0
    new_board = board if move is None else make_move(board, move, player)
    new_state = (new_board, new_player, new_consecutive_passes)
    return new_state


def is_gameover(board, player):
    possible_moves = get_possible_moves(board,  player)
    if possible_moves:
        return False
    
    opponent = 'w' if player == 'b' else 'b'
    opponents_moves = get_possible_moves(board, opponent)
    if opponents_moves:
        return False
    return True


def get_winner(board):
    white_pieces = sum(row.count('w') for row in board)
    black_pieces = sum(row.count('b') for row in board)
    if white_pieces == black_pieces:
        return None
    if white_pieces > black_pieces:
        return "white"
    else:
        return "black"