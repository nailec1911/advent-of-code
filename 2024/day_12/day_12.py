f = [e[:-1] for e in list(open("input.txt"))]

def replace1_dot(f, b):
    for z in range(b[0], b[1] + 1):
        for w in range(b[2], b[3] + 1):
            if f[z][w] == '1': f[z][w] = '.'

def get_sides(f, limits):
    top, bot ,left, right = limits
    res = [
        [[] for _ in range(bot - top + 1)],
        [[] for _ in range(bot - top + 1)],
        [[] for _ in range(right - left + 1)],
        [[] for _ in range(right - left + 1)],
    ]
    for i in range(top, bot + 1):
        for j in range(left, right + 1):
            if f[i][j] == '1' and (j == 0 or f[i][j - 1] != '1'):
                res[0][i - top].append(j)
            if f[i][j] == '1' and (j + 1 >= len(f[0]) or f[i][j + 1] != '1'):
                res[1][i - top].append(j)
            if f[i][j] == '1' and (i == 0 or f[i - 1][j] != '1'):
                res[2][j - left].append(i)
            if f[i][j] == '1' and (i + 1 >= len(f) or f[i + 1][j] != '1'):
                res[3][j - left].append(i)
    return res


def get_shape(f, i, j):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    searched = f[i][j]
    limits = [i, i, j, j]
    area = 0

    def flood(x, y):
        nonlocal area
        if not(0 <= x < len(f) and 0 <= y < len(f[0])):
            return
        if not f[x][y] == searched:
            return
        if x < limits[0]: limits[0] = x
        if x > limits[1]: limits[1] = x
        if y < limits[2]: limits[2] = y
        if y > limits[3]: limits[3] = y
        f[x][y] = '1'
        area += 1
        for k,r in dirs:
            flood(x + k, y + r)

    flood(i, j)
    sides = get_sides(f, limits)
    replace1_dot(f, limits)
    return area, sides

def get_tot_side(sides):
    tot = 0
    for side in sides:
        for i in range(len(side)):
            while side[i]:
                tot += 1
                elt = side[i].pop()
                j = i + 1
                while j < len(side) and elt in side[j]:
                    side[j].remove(elt)
                    j += 1
    return tot


f = [list(e) for e in f]
score = 0
score2 = 0
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '.':
            continue
        area, sides = get_shape(f, i, j)
        circumference = sum([len(val) for side in sides for val in side])
        score += circumference * area
        score2 += get_tot_side(sides) * area


print(score, score2)
