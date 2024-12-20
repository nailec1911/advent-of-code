def find_path(f, x, y, end_x, end_y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    score = 0

    while x != end_x or y != end_y:
        f[x][y] = score
        score += 1

        for dx, dy in directions:
            if f[x + dx][y + dy] == '.' or f[x + dx][y + dy] == 'E':
                f[x + dx][y + dy] = score
                x += dx
                y += dy
                break
    return score


f = [e[:-1] for e in list(open("input.txt"))]

start_x, start_y = 0, 0
end_x, end_y = 0, 0
for x, line in enumerate(f):
    yt = line.find('S')
    if yt != -1:
        start_x, start_y = x, yt
    end_yt = line.find('E')
    if end_yt != -1:
        end_x, end_y = x, end_yt

f = [list(e) for e in f]
find_path(f, start_x, start_y, end_x, end_y)


def get_score(f, size_shortcut):
    shortcut_pos = set()
    for i in range(size_shortcut):
        for j in range(0, size_shortcut - i):
            shortcut_pos.add((i, j))
            shortcut_pos.add((i, -j))
            shortcut_pos.add((-i, j))
            shortcut_pos.add((-i, -j))

    score = 0
    for i, l in enumerate(f):
        for j, start in enumerate(l):
            if not isinstance(start, int):
                continue
            for x, y in shortcut_pos:
                tx, ty = i + x, j + y
                if not (0 <= tx < len(f) and 0 <= ty < len(f[0])):
                    continue
                if not isinstance(f[tx][ty], int):
                    continue
                if start > f[tx][ty]:
                    continue
                dist = abs(x + y)
                dist = f[tx][ty] - start - abs(x) - abs(y)
                if dist >= 100:
                    score += 1
    return score


print(get_score(f, 3))
print(get_score(f, 21))
