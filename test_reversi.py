import pytest
from reversi import (
    generate_start_board,
    check_direction,
    is_outside,
    get_flips_in_direction,
    make_move,
    get_possible_moves,
    map_sign,
    check_move,
    update_state,
    is_gameover,
    get_winner,
)


@pytest.fixture
def start_board():
    return [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', 'o', ' ', ' ', ' '],
        [' ', ' ', ' ', 'o', 'x', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]


@pytest.fixture
def diagonal_board():
    return [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', 'o', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', 'o', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]


@pytest.fixture
def mid_game_board():
    return [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'x', 'o', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', 'x', 'o', ' ', ' ', ' '],
        [' ', ' ', ' ', 'o', 'x', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]


def test_generating_start_board(start_board):
    generated_start_board = generate_start_board()
    assert generated_start_board == start_board


def test_is_outside():
    assert is_outside((-1, 0)) is True
    assert is_outside((0, -1)) is True
    assert is_outside((8, 0)) is True
    assert is_outside((0, 8)) is True
    assert is_outside((0, 0)) is False
    assert is_outside((7, 7)) is False


def test_check_direction(start_board):
    result = check_direction((start_board, 'o'), (3, 2), (0, 1))
    assert result == (3, 4)
    result = check_direction((start_board, 'x'), (3, 5), (0, -1))
    assert result == (3, 3)
    result = check_direction((start_board, 'o'), (2, 3), (1, 0))
    assert result == (4, 3)
    result = check_direction((start_board, 'x'), (5, 3), (-1, 0))
    assert result == (3, 3)
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', 'x', 'o', ' ', ' '],
        [' ', ' ', ' ', 'o', 'x', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    result = check_direction((board, 'o'), (3, 2), (0, 1))
    assert result == (3, 5)


def test_check_direction_diagonal(diagonal_board):
    result = check_direction((diagonal_board, 'o'), (2, 2), (1, 1))
    assert result == (4, 4)
    result = check_direction((diagonal_board, 'x'), (2, 5), (1, -1))
    assert result == (4, 3)
    result = check_direction((diagonal_board, 'o'), (5, 2), (-1, 1))
    assert result == (3, 4)
    result = check_direction((diagonal_board, 'x'), (5, 5), (-1, -1))
    assert result == (3, 3)


def test_check_direction_empty(start_board):
    result = check_direction((start_board, 'o'), (1, 1), (0, 1))
    assert result is None
    result = check_direction((start_board, 'x'), (3, 5), (0, 1))
    assert result is None
    result = check_direction((start_board, 'o'), (0, 0), (-1, -1))
    assert result is None
    result = check_direction((start_board, 'x'), (7, 7), (1, 1))
    assert result is None


def test_get_flips_in_direction(start_board):
    flips = get_flips_in_direction((0, 1), (start_board, 'o'), (3, 2))
    assert flips == [(3, 3)]

    flips = get_flips_in_direction((0, -1), (start_board, 'x'), (3, 5))
    assert flips == [(3, 4)]

    flips = get_flips_in_direction((1, 0), (start_board, 'o'), (2, 3))
    assert flips == [(3, 3)]

    flips = get_flips_in_direction((1, 1), (start_board, 'x'), (0, 0))
    assert flips == []


def test_make_move(start_board):
    new_board = make_move((start_board, 'o'), (3, 2))

    assert new_board[3][2] == 'o'
    assert new_board[3][3] == 'o'


def test_make_move_multiple_flips():
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', 'o', 'o', 'o', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    new_board = make_move((board, 'x'), (2, 4))

    assert new_board[2][1] == 'x'
    assert new_board[2][2] == 'x'
    assert new_board[2][3] == 'x'
    assert new_board[2][4] == 'x'


def test_make_move_flips_many_directions():
    board = [
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' '],
        ['x', 'o', 'o', ' ', 'o', 'o', 'x', ' '],
        [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    new_board = make_move((board, 'x'), (3, 3))

    assert new_board[3][3] == 'x'
    assert new_board[2][3] == 'x'
    assert new_board[4][3] == 'x'
    assert new_board[3][2] == 'x'
    assert new_board[3][4] == 'x'


def test_get_possible_moves(start_board):
    moves = get_possible_moves((start_board, 'o'))

    assert len(moves) > 0
    moves_white = [(2, 3), (3, 2), (4, 5), (5, 4)]
    for move in moves_white:
        assert move in moves

    moves = get_possible_moves((start_board, 'x'))
    assert len(moves) > 0
    moves_black = [(2, 4), (3, 5), (4, 2), (5, 3)]
    for move in moves_black:
        assert move in moves


def test_map_sign():
    assert map_sign(-10) == -1
    assert map_sign(-1) == -1
    assert map_sign(0) == 0
    assert map_sign(1) == 1
    assert map_sign(100) == 1


def test_check_move(start_board):
    assert check_move((start_board, 'o'), (3, 2), (0, 1)) == (3, 2)
    assert check_move((start_board, 'o'), (0, 0), (0, 1)) is None
    assert check_move((start_board, 'x'), (3, 5), (0, -1)) == (3, 5)


def test_update_state_move(start_board):
    state = (start_board, 'o')
    new_board, new_player = update_state(state, (3, 2))

    assert new_player == 'x'
    assert new_board[3][2] == 'o'
    assert new_board[3][3] == 'o'


def test_is_gameover_full_board():
    board = [['x'] * 8 for _ in range(8)]

    assert is_gameover((board, 'x')) is True


def test_is_gameover_start_position(start_board):
    assert is_gameover((start_board, 'x')) is False
    assert is_gameover((start_board, 'o')) is False


def test_is_gameover_draw_position():
    board = [['x', 'o'] * 4 for _ in range(8)]

    assert is_gameover((board, 'x')) is True


def test_get_winner_x():
    board = [['x'] * 8 for _ in range(8)]

    assert get_winner(board) == "x"


def test_get_winner_o():
    board = [['o'] * 8 for _ in range(8)]

    assert get_winner(board) == "o"


def test_get_winner_draw():
    board = [['x'] * 4 + ['o'] * 4 for _ in range(8)]

    assert get_winner(board) is None