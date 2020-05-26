from pprint import pprint


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]


size = 11
board = create_board(size)
y, x = size // 2, size // 2

cordinate = (-1, 0)


direction = "L" if board[x][y] else "R"

cord_moves = {
    "R": {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)},
    "L": {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
}


for _ in range(200):
    field = board[y][x]
    direction = "L" if field else "R"
    board[y][x] = 0 if field else 1
    cordinate = cord_moves[direction][cordinate]
    y, x = y + cordinate[0], x + cordinate[1]

for row in board:
    for field in row:
        print(f"[{'█' if field else ' '}]", end="")
    print()
