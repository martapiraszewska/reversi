def get_starting_piece(i, j):
    if (i == 3 and j == 3) or (i == 4 and j == 4):
        return 'x'
    elif (i == 3 and j == 4) or (i == 4 and j == 3):
        return 'o'
    return ' '


def generate_start_board():
    rows, cols = 8, 8
    board = [[get_starting_piece(i, j) for j in range(cols)] for i in range(rows)]
    return board


def get_start_state():
    board = generate_start_board()
    curr_player = 'x'
    state = (board, curr_player)
    return state


def is_outside(cell):
    x, y = cell
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return True
    return False


def check_direction(state, cell, direction):
    board, player = state
    next_cell = tuple(map(lambda x, y: x + y, cell, direction))
    if is_outside(next_cell):
        return None
    x, y = next_cell
    if board[x][y] == ' ':
        return None
    elif board[x][y] != player:
        end_cell = check_direction(state, next_cell, direction)
    else:
        return next_cell
    return end_cell


def map_sign(number):
    if number == 0:
        return 0
    if number < 0:
        return -1
    return 1


def get_flips_in_direction(direction, state, move_cell):
    end_cell = check_direction(state, move_cell, direction)
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
    if cell_state == ' ':
        return player
    elif cell_state == 'x':
        return 'o'
    return 'x'


def generate_new_board(state, pieces_to_flip):
    board, player = state
    new_board = [
        [update_cell(pieces_to_flip, (i, j), col, player) for j, col in enumerate(row)] for i, row in enumerate(board)]
    return new_board


def make_move(state, move_cell):
    directions = [
        (-1, 0), (1, 0),    # up and down
        (0, -1), (0, 1),    # left and right
        (-1, -1), (-1, 1),   # diagonal
        (1, -1), (1, 1),
    ]
    pieces_to_flip = [get_flips_in_direction(direction, state, move_cell) for direction in directions]
    flatten_pieces = [piece for row in pieces_to_flip for piece in row]
    all_pieces_to_flip = set(flatten_pieces + [move_cell])
    new_board = generate_new_board(state, all_pieces_to_flip)
    return new_board


def check_move(state, move_cell, direction):
    x, y = move_cell
    end_cell = check_direction(state, move_cell, direction)
    if end_cell is not None:
        end_x, end_y = end_cell
        if abs(x - end_x) > 1 or abs(y - end_y) > 1:
            return move_cell
    return None


def get_possible_moves(state):
    board, _ = state
    empty_cells = [[(i, j) for j, col in enumerate(row) if col == ' '] for i, row in enumerate(board)]
    empty_cells_flatten = [cell for row in empty_cells for cell in row]
    directions = [
        (-1, 0), (1, 0),    # up and down
        (0, -1), (0, 1),    # left and right
        (-1, -1), (-1, 1),   # diagonal
        (1, -1), (1, 1),
    ]
    moves = [
        check_move(state, cell, direction) for cell in empty_cells_flatten for direction in directions]
    moves_without_none = [move for move in moves if move is not None]
    moves_without_duplicates = list(set(moves_without_none))
    return moves_without_duplicates


def update_state(state, move):
    board, player = state
    new_player = 'x' if player == 'o' else 'o'
    new_board = board if move is None else make_move(state, move)
    new_state = (new_board, new_player)
    return new_state


def is_gameover(state):
    board, player = state
    possible_moves = get_possible_moves(state)
    if possible_moves:
        return False
    
    opponent = 'o' if player == 'x' else 'x'
    new_state = (board, opponent)
    opponents_moves = get_possible_moves(new_state)
    if opponents_moves:
        return False
    return True


def get_winner(board):
    o_pieces = sum(row.count('o') for row in board)
    x_pieces = sum(row.count('x') for row in board)
    if o_pieces == x_pieces:
        return None
    if o_pieces > x_pieces:
        return "o"
    else:
        return "x"