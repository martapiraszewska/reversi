import pytest
from reversi import (
    generate_start_board,
    check_direction,
    is_outside,
    get_flips_in_direction,
    make_move,
    get_possible_moves,
)


@pytest.fixture
def start_board():
    return [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'b', 'w', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'w', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]


@pytest.fixture
def diagonal_board():
    return [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'b', 'w', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'b', 'w', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]


@pytest.fixture
def mid_game_board():
    return [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'w', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'w', 'b', 'w', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'w', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
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
    result = check_direction(start_board, (3, 2), (0, 1), 'w')
    assert result == (3, 4)
    result = check_direction(start_board, (3, 5), (0, -1), 'b')
    assert result == (3, 3)
    result = check_direction(start_board, (2, 3), (1, 0), 'w')
    assert result == (4, 3)
    result = check_direction(start_board, (5, 3), (-1, 0), 'b')
    assert result == (3, 3)

    board = [
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'b', 'b', 'w', 'e', 'e'],
        ['e', 'e', 'e', 'w', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ]
    result = check_direction(board, (3, 2), (0, 1), 'w')
    assert result == (3, 5)


def test_check_direction_diagonal(diagonal_board):
    result = check_direction(diagonal_board, (2, 2), (1, 1), 'w')
    assert result == (4, 4)
    result = check_direction(diagonal_board, (2, 5), (1, -1), 'b')
    assert result == (4, 3)
    result = check_direction(diagonal_board, (5, 2), (-1, 1), 'w')
    assert result == (3, 4)
    result = check_direction(diagonal_board, (5, 5), (-1, -1), 'b')
    assert result == (3, 3)


def test_check_direction_empty(start_board):
    result = check_direction(start_board, (1, 1), (0, 1), 'w')
    assert result is None
    result = check_direction(start_board, (3, 5), (0, 1), 'b')
    assert result is None
    result = check_direction(start_board, (0, 0), (-1, -1), 'w')
    assert result is None
    result = check_direction(start_board, (7, 7), (1, 1), 'b')
    assert result is None


def test_get_flips_in_direction(start_board):
    flips = get_flips_in_direction((0, 1), start_board, (3, 2), 'w')
    assert flips == [(3, 3)]

    flips = get_flips_in_direction((0, -1), start_board, (3, 5), 'b')
    assert flips == [(3, 4)]

    flips = get_flips_in_direction((1, 0), start_board, (2, 3), 'w')
    assert flips == [(3, 3)]

    flips = get_flips_in_direction((1, 1), start_board, (0, 0), 'w')
    assert flips == []


def test_make_move(start_board):
    new_board = make_move(start_board, (3, 2), 'w')

    assert new_board[3][2] == 'w'
    assert new_board[3][3] == 'w'


def test_get_possible_moves(start_board):
    moves = get_possible_moves(start_board, 'w')

    assert len(moves) > 0
    moves_white = [(2, 3), (3, 2), (4, 5), (5, 4)]
    for move in moves_white:
        assert move in moves

    moves = get_possible_moves(start_board, 'b')
    assert len(moves) > 0
    moves_black = [(2, 4), (3, 5), (4, 2), (5, 3)]
    for move in moves_black:
        assert move in moves
