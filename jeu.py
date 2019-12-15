import time

EMPTY = 0
BALL = 1
INVALID = 9

best = None
start_time = time.time()


def print_board(board):
    m = {EMPTY: ". ", BALL: "O ", INVALID: "  "}
    for row in board:
        print("".join([m[c] for c in row]))


def copy_board(board):
    return [row[:] for row in board]


def try_all_directions(board, x, y, path):
    locked = True

    # Try move up
    if y >= 2 and board[y - 1][x] == BALL and board[y - 2][x] == EMPTY:
        new_board = copy_board(board)
        new_board[y][x] = EMPTY
        new_board[y - 1][x] = EMPTY
        new_board[y - 2][x] = BALL
        locked = False
        try_all_balls(new_board, path[:] + [(x, y, x, y - 2)])

    # Try move down
    if y < len(board) - 2 and board[y + 1][x] == BALL and board[y + 2][x] == EMPTY:
        new_board = copy_board(board)
        new_board[y][x] = EMPTY
        new_board[y + 1][x] = EMPTY
        new_board[y + 2][x] = BALL
        locked = False
        try_all_balls(new_board, path[:] + [(x, y, x, y + 2)])

    # Try move left
    if x >= 2 and board[y][x - 1] == BALL and board[y][x - 2] == EMPTY:
        new_board = copy_board(board)
        new_board[y][x] = EMPTY
        new_board[y][x - 1] = EMPTY
        new_board[y][x - 2] = BALL
        locked = False
        try_all_balls(new_board, path[:] + [(x, y, x - 2, y)])

    # Try move right
    if x < len(board[y]) - 2 and board[y][x + 1] == BALL and board[y][x + 2] == EMPTY:
        new_board = copy_board(board)
        new_board[y][x] = EMPTY
        new_board[y][x + 1] = EMPTY
        new_board[y][x + 2] = BALL
        locked = False
        try_all_balls(new_board, path[:] + [(x, y, x + 2, y)])

    return locked


def try_all_balls(board, path):
    global best
    global start_time
    all_locked = True
    remaining = 0

    for y in range(len(board)):
        row = board[y]
        for x in range(len(row)):
            if row[x] == BALL:
                remaining += 1
                locked = try_all_directions(board, x, y, path)
                if not locked:
                    all_locked = False
    if all_locked:
        if best is None or remaining < best:
            best = remaining
            elapsed = time.time() - start_time
            print(f"Remaining: {remaining} ({elapsed})")
            print_board(board)
            print("Path: ")
            print(", ".join(f"[{p[0]}, {p[1]} => {p[2]}, {p[3]}]" for p in path))
            print()


def main():
    board = [
        "  OOO  ",
        " OOOOO ",
        "OO...OO",
        "OO...OO",
        "OO...OO",
        " OOOOO ",
        "  OOO  ",
    ]

    xboard = [
        "  OOO  ",
        "  OOO  ",
        "OOOOOOO",
        "OOO.OOO",
        "OOOOOOO",
        "  OOO  ",
        "  OOO  ",
    ]

    # board = [" OOO ", "OOOOO", "OOOOO", "OOOOO", " OO. "]
    # board = ["OO."]
    # board = ["O", "O", "."]

    m = {" ": INVALID, "O": BALL, ".": EMPTY}
    board = [[m[c] for c in row] for row in board]

    print_board(board)
    try_all_balls(board, [])


main()
