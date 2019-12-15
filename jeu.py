import time

EMPTY = 0
BALL = 1
INVALID = 9

best = None
start_time = time.time()
visited = set()


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


def is_visited(board):
    if tuple(a for b in board for a in b) in visited:
        return True

    if tuple(a for b in board for a in reversed(b)) in visited:
        return True

    if tuple(a for b in reversed(board) for a in b) in visited:
        return True

    if tuple(a for b in reversed(board) for a in reversed(b)) in visited:
        return True

    rows = len(board)
    cols = len(board[0])
    rot = tuple(tuple(board[x][y] for x in range(cols)) for y in range(rows))

    if tuple(a for b in rot for a in b) in visited:
        return True

    if tuple(a for b in rot for a in reversed(b)) in visited:
        return True

    if tuple(a for b in reversed(rot) for a in b) in visited:
        return True

    if tuple(a for b in reversed(rot) for a in reversed(b)) in visited:
        return True

    return False


def add_to_visited(board):
    visited.add(tuple(a for b in board for a in b))


def try_all_balls(board, path):
    global best
    global start_time
    all_locked = True
    remaining = 0

    if is_visited(board):
        return

    add_to_visited(board)

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
    ysb_board = [
        "  OOO  ",
        " OOOOO ",
        "OO...OO",
        "OO...OO",
        "OO...OO",
        " OOOOO ",
        "  OOO  ",
    ]

    classic_board = [
        "  OOO  ",
        "  OOO  ",
        "OOOOOOO",
        "OOO.OOO",
        "OOOOOOO",
        "  OOO  ",
        "  OOO  ",
    ]

    board = ysb_board

    m = {" ": INVALID, "O": BALL, ".": EMPTY}
    board = [[m[c] for c in row] for row in board]

    print_board(board)
    try_all_balls(board, [])

    elapsed = time.time() - start_time
    print(f"All solutions tested in {elapsed} seconds. Best: {best} remaining balls.")


main()
