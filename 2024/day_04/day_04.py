f = [e[:-1] for e in list(open("input.txt"))]

# f = [
# "MMMSXXMASM",
# "MSAMXMSMSA",
# "AMXSXMAAMM",
# "MSAMASMSMX",
# "XMASAMXAMM",
# "XXAMMXXAMA",
# "SMSMSASXSS",
# "SAXAMASAAA",
# "MAMMMXMMMM",
# "MXMXAXMASX",
# ]


def hor(f, i, j):
    t = False
    b = False
    if j + 4 < len(f[0]) and f[i][j:j + 4] == 'XMAS':
        b = True
    if j - 4 >= 0 and f[i][j:j - 4:-1] == 'XMAS':
        t = True
    return [b, t]

def ver(f, i, j):
    s = 'XMAS'
    t = True
    b = True
    for k in range(4):
        if i + k  >= len(f) or f[i + k][j] != s[k]:
            b = False
        if i < k < 0 or f[i - k][j] != s[k]:
            t = False
    return [b, t]


def diag(f, i, j):
    s = 'XMAS'
    t = True
    t1 = True
    b = True
    b1 = True
    for k in range(4):
        if i - k < 0 or j - k < 0 or f[i - k][j - k] != s[k]:
            b = False
        if i + k  >= len(f) or j - k < 0   or f[i + k][j - k] != s[k]:
            t = False
        if i + k  >= len(f) or j + k >= len(f[0]) or f[i + k][j + k] != s[k]:
            b1 = False
        if i - k < 0 or j + k >= len(f[0]) or f[i - k][j + k] != s[k]:
            t1 = False
    return [t, t1, b, b1]


def cross(f, i, j):
    if not (0 < i < len(f) - 1 and 0 < j < len(f[0]) - 1):
        return False
    if f[i - 1][j - 1] == "M" and f[i - 1][j + 1] == "S" and f[i][j] == "A"\
        and f[i + 1][j - 1] == "M" and f[i + 1][j + 1] == "S":
        return True
    if f[i - 1][j - 1] == "M" and f[i - 1][j + 1] == "M" and f[i][j] == "A"\
        and f[i + 1][j - 1] == "S" and f[i + 1][j + 1] == "S":
        return True
    if f[i - 1][j - 1] == "S" and f[i - 1][j + 1] == "M" and f[i][j] == "A"\
        and f[i + 1][j - 1] == "S" and f[i + 1][j + 1] == "M":
        return True
    if f[i - 1][j - 1] == "S" and f[i - 1][j + 1] == "S" and f[i][j] == "A"\
        and f[i + 1][j - 1] == "M" and f[i + 1][j + 1] == "M":
        return True
    return False

score: int = 0
score2: int = 0
for i in range(len(f)):
    for j in range(len(f[i])):
        h = hor(f, i, j)
        v = ver(f, i, j)
        d = diag(f, i, j)
        total = h + v + d
        score += total.count(True)
        if cross(f, i, j):
            score2 += 1

print(score)
print(score2)
