initial = {
    13: 5,
    14: 6,
    16: 1,
    17: 9,
    21: 4,
    22: 1,
    23: 7,
    24: 8,
    29: 6,
    30: 1,
    31: 9,
    33: 7,
    34: 4,
    36: 2,
    37: 9,
    46: 2,
    47: 7,
    54: 8,
    60: 5,
    67: 4,
    69: 2,
    71: 1,
    74: 3,
    76: 7,
    77: 8,
    79: 5,
    80: 2,
}

board = [initial.get(i + 1, 0) for i in range(81)]


def is_column(i, j):
    return (i - j) % 9 == 0


def is_row(i, j):
    return i / 9 == j / 9


def is_block(i, j):
    return i / 27 == j / 27 and (i % 9) / 3 == (j % 9) / 3


def solve(board):
    try:
        i = board.index(0)
    except:
        return board

    excluded_numbers = set()
    for j in range(81):
        if is_row(i, j) or is_column(i, j) or is_block(i, j):
            excluded_numbers.add(board[j])

    for m in '123456789':
        if int(m) not in excluded_numbers:
            print int(m)
            board[i] = int(m)
            print board
            return solve(board)


if __name__ == "__main__":
    print len(board)
    print solve(board)
