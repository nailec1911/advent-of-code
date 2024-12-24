import heapq
from collections import deque
from numba import jit
f = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############",
]


f = [
    "#################",
    "#...#...#...#..E#",
    "#.#.#.#.#.#.#.#.#",
    "#.#.#.#...#...#.#",
    "#.#.#.#.###.#.#.#",
    "#...#.#.#.....#.#",
    "#.#.#.#.#.#####.#",
    "#.#...#.#.#.....#",
    "#.#.#####.#.###.#",
    "#.#.#.......#...#",
    "#.#.###.#####.###",
    "#.#.#...#.....#.#",
    "#.#.#.#####.###.#",
    "#.#.#.........#.#",
    "#.#.#.#########.#",
    "#S#.............#",
    "#################",
]

def get_score(f, x, y):
    pq = []
    heapq.heappush(pq, (0, x, y, '>', []))

    visited = set()
    visited.add((x, y, '>'))
    best_paths = []
    best_score = float('inf')

    while pq:
        s, x, y, d, path = heapq.heappop(pq)

        if s > best_score:
            continue

        if x == 1 and y == len(f[0]) - 2:
            if s < best_score:
                best_score = s
                best_paths = [path + [(x, y)]]
            elif s == best_score:
                best_paths.append(path + [(x, y)])
            continue

        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(f) and 0 <= ny < len(f[0]) and f[nx][ny] != '#':
            if (nx, ny, d) not in visited:
                visited.add((nx, ny, d))
                heapq.heappush(pq, (s + 1, nx, ny, d, path + [(x, y)]))

        to_test = '><'
        if d == '>' or d == '<':
            to_test = '^v'
        for new_dir in to_test:
            if (x, y, new_dir) not in visited:
                visited.add((x, y, new_dir))
                heapq.heappush(pq, (s + 1000, x, y, new_dir, path))
    best_path_tiles = set()
    for path in best_paths:
        best_path_tiles.update(path)
    return best_score, best_path_tiles


def print_path(f, path):
    for i in range(len(f)):
        for j in range(len(f[0])):
            if (i, j) in path:
                print('O', end='')
            elif f[i][j] == '#':
                print('#', end='')
            else:
                print('.', end='')
        print()


directions = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
f = [e[:-1] for e in list(open("input.txt"))]
f = [list(e) for e in f]
x, y = len(f) - 2, 1

score1, path = get_score(f, x, y)
total_path = set(path)
i = 0
for dx, dy in path:
    print(i, len(path))
    i += 1
    f[dx][dy] = '#'
    score2, path2 = get_score(f, x, y)
    if score2 == score1:
        for e in path2:
            total_path.add(e)
    f[dx][dy] = '.'

print_path(f, total_path)
print(score1)
print(len(total_path))
