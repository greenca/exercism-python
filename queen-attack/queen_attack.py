def board(pos1, pos2):

    check_positions(pos1, pos2)

    board = []
    for i in range(8):
        row = 8*['_']
        if i == pos1[0]:
            row[pos1[1]] = 'W'
        if i == pos2[0]:
            row[pos2[1]] = 'B'
        board.append(''.join(row))
    return board


def can_attack(pos1, pos2):

    check_positions(pos1, pos2)

    # Check for same row
    if pos1[0] == pos2[0]:
        return True

    # Check for same column
    if pos1[1] == pos2[1]:
        return True

    # Check for diagonal
    row_diff = pos1[0] - pos2[0]
    col_diff = pos1[1] - pos2[1]
    if row_diff == col_diff or row_diff == -col_diff:
        return True

    return False


def check_positions(pos1, pos2):
    if pos1 == pos2:
        raise ValueError("Cannot have two queens in the same square")
    if min(pos1) < 0 or min(pos2) < 0:
        raise ValueError("Indices must be greater or equal to 0")
    if max(pos1) > 7 or max(pos2) > 7:
        raise ValueError("Indices must be less than or equal to 7")

