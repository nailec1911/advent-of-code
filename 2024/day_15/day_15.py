def print_map(board):
    print(*[''.join(e) for e in board], sep='\n')


def get_score(board, search):
    score = 0
    for top, l in enumerate(board):
        for side, c in enumerate(l):
            if c == search:
                score += 100 * top + side
    return score


def push_single_box(board, bx, by, x, y, chars) -> bool:
    ty = by
    tx = bx
    while board[tx][ty] in chars:
        ty += y
        tx += x
    if board[tx][ty] != '.':
        return False
    while ty != by or tx != bx:
        board[tx][ty] = board[tx - x][ty - y]
        ty -= y
        tx -= x
    board[bx][by] = '.'
    return True


def can_push(board, bx, by, x):
    if board[bx][by] == '.':
        return True
    byy = by + 1
    if board[bx][by] == ']':
        byy = by - 1

    a, b = False, False
    if board[bx + x][by] in '.[]':
        a = can_push(board, bx + x, by, x)
    if board[bx + x][byy] in '.[]':
        b = can_push(board, bx + x, byy, x)
    return a and b


def push_box2y(board, bx, by, x):
    byy = by + 1
    if board[bx][by] == ']':
        byy = by - 1

    if board[bx + x][by] in '[]':
        push_box2y(board, bx + x, by, x)
    if board[bx + x][byy] in '[]':
        push_box2y(board, bx + x, byy, x)

    if board[bx + x][by] != '.' or board[bx + x][byy] != '.':
        return
    board[bx + x][by] = board[bx][by]
    board[bx + x][byy] = board[bx][byy]
    board[bx][by] = '.'
    board[bx][byy] = '.'


f = [e[:-1] for e in list(open("input.txt"))]
separator = f.index('')

dirs = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
board1 = [list(e) for e in f[:separator]]

MOVES = ''.join(f[separator + 1:])

board2 = []
ax, ay, ax2, ay2 = 0, 0, 0, 0
for i, line in enumerate(board1):
    line = ''.join(line)
    if (x := line.find('@')) != -1:
        ax, ay = i, x
    line = line.replace('.', '..')
    line = line.replace('#', '##')
    line = line.replace('O', '[]')
    line = line.replace('@', '@.')
    board2.append(list(line))

ax2, ay2 = ax, ay * 2
for move in MOVES:
    x, y = dirs[move]
    tx, ty = ax + x, ay + y

    push_single_box(board1, tx, ty, x, y, 'O')
    if board1[tx][ty] == '.':
        board1[ax][ay] = '.'
        ax += x
        ay += y
        board1[ax][ay] = '@'

    tx, ty = ax2 + x, ay2 + y
    if x == 0:
        push_single_box(board2, tx, ty, x, y, '[]')
    if y == 0 and can_push(board2, tx, ty, x):
        push_box2y(board2, tx, ty, x)
    if board2[tx][ty] == '.':
        board2[ax2][ay2] = '.'
        ax2 += x
        ay2 += y
        board2[ax2][ay2] = '@'


print(get_score(board1, 'O'))
print(get_score(board2, '['))
