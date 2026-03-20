def get_starting_piece(i, j):
    if (i == 3 and j == 3) or (i == 4 and j == 4):
        return "b"
    elif (i == 3 and j == 4) or (i == 4 and j == 3):
        return "w"
    return "e"


def generate_start_board():
    rows, cols = 8, 8
    board = [[get_starting_piece(i, j) for j in range(cols)] for i in range(rows)]
    return board


def is_outside(position):
    x, y = position
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return True
    return False


def check_direction(board, position, direction, player):
    next_pos = tuple(map(lambda x, y: x + y, position, direction))
    if is_outside(next_pos):
        return None
    x, y = next_pos
    if board[x][y] == 'e':
        return None
    elif board[x][y] != player:
        end_pos = check_direction(board, next_pos, direction, player)
    else:
        return next_pos
    return end_pos


def map_sign(number):
    if number == 0:
        return 0
    if number < 0:
        return -1
    return 1


def update_cell(pieces_to_flip, x, y, val, player):
    if (x, y) not in pieces_to_flip:
        return val
    if val == 'e':
        return player
    elif val == 'b':
        return 'w'
    return 'b'


def generate_new_board(board, pieces_to_flip, player):
    new_board = [
        [update_cell(pieces_to_flip, i, j, col, player) for j, col in enumerate(row)] for i, row in enumerate(board)]
    return new_board


def get_flips_in_direction(direction, board, move_pos, player):
    end_position = check_direction(board, move_pos, direction, player)
    if end_position is not None:
        x, y = move_pos
        end_x, end_y = end_position
        if abs(x - end_x) > 1 or abs(y - end_y) > 1:
            dx = map_sign(end_x - x)
            dy = map_sign(end_y - y)
            distance = max(abs(end_x - x), abs(end_y - y))
            pieces_to_flip = [(x + k * dx, y + k * dy) for k in range(1, distance)]
            return pieces_to_flip
    return []


def make_move(board, move_pos, player):
    directions = [
        (-1, 0), (1, 0),    # up and down
        (0, -1), (0, 1),    # left and right
        (-1, -1), (-1, 1),   # diagonal
        (1, -1), (1, 1),
    ]
    pieces_to_flip = [get_flips_in_direction(direction, board, move_pos, player) for direction in directions]
    flatten_pieces = [piece for row in pieces_to_flip for piece in row]
    all_pieces_to_flip = set(flatten_pieces + [move_pos])
    new_board = generate_new_board(board, all_pieces_to_flip, player)
    return new_board


def check_move(board, square, direction, player):
    x, y = square
    pos = check_direction(board, square, direction, player)
    if pos is not None:
        end_x, end_y = pos
        if abs(x - end_x) > 1 or abs(y - end_y) > 1:
            return square
    return None


def get_possible_moves(board, player):
    empty_squares = [[(i, j) for j, col in enumerate(row) if col == 'e'] for i, row in enumerate(board)]
    empty_squares_flatten = [square for row in empty_squares for square in row]
    directions = [
        (-1, 0), (1, 0),    # up and down
        (0, -1), (0, 1),    # left and right
        (-1, -1), (-1, 1),   # diagonal
        (1, -1), (1, 1),
    ]
    moves = [
        check_move(board, square, direction, player) for square in empty_squares_flatten for direction in directions]
    moves_without_none = [move for move in moves if move is not None]
    moves_without_duplicates = list(set(moves_without_none))
    return moves_without_duplicates
