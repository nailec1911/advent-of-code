import heapq


def get_shortest_path(f, size_x, size_y):
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    pq = []
    heapq.heappush(pq, (0, 0, 0))

    visited = set()
    visited.add((0, 0, '>'))
    best_score = float('inf')

    while pq:
        s, x, y = heapq.heappop(pq)

        if s > best_score:
            continue

        if x == size_x - 1 and y == size_y - 1:
            if s < best_score:
                best_score = s
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE_X and 0 <= ny < SIZE_Y and f[nx][ny] != '#':
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(pq, (s + 1, nx, ny))
    return best_score


f = [e[:-1] for e in list(open("input.txt"))]

for i, e in enumerate(f):
    a, b = e.split(',')
    f[i] = [int(a), int(b)]

SIZE_X = 71
SIZE_Y = 71
STOP = 1024
board = [['.' for i in range(SIZE_Y)] for j in range(SIZE_X)]

for i, (y, x) in enumerate(f):
    if i >= STOP:
        break
    board[x][y] = '#'

score = get_shortest_path(board, SIZE_X, SIZE_Y)
print(score)

for y, x in f[STOP:]:
    board[x][y] = '#'

    if get_shortest_path(board, SIZE_X, SIZE_Y) == float('inf'):
        print(y, x)
        break
