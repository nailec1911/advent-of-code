from math import gcd

f = [e[:-1] for e in list(open("input.txt"))]

def get_all_pos(f, freq):
    res = []
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == freq:
                res.append([i, j])
    return res


def loop_dir(ox, oy, x, y, size_x, size_y):
    diff = gcd(x, y)
    xd,yd = x // diff, y // diff
    res = []
    i = 0
    while (0 <= ox + xd * i < size_x and 0 <= oy + yd * i < size_y):
        res.append([ox + xd * i, oy + yd * i])
        i += 1
    return res

def get_antinodes(elt, others, size_x, size_y):
    l1, l2 = [], []
    x,y = elt
    for e in others:
        xe, ye = e
        xd, yd = xe - x, ye - y
        if 0 <= x - xd < size_x and 0 <= y - yd < size_y:
            l1.append([x - xd, y - yd])
        if 0 <= xe + xd < size_x and 0 <= ye + yd < size_y:
            l1.append([xe + xd, ye + yd])
        l2 += loop_dir(x, y, -xd, -yd, size_x, size_y)
        l2 += loop_dir(xe, ye, xd, yd, size_x, size_y)
    return l1, l2


freqs = {}
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '.' or f[i][j] == '#' or f[i][j] in freqs.keys():
            continue
        freqs[f[i][j]] = get_all_pos(f, f[i][j])


antinodes = []
antinodes2 = []
size_x = len(f)
size_y = len(f[0])
for freq, poss in freqs.items():
    for i in range(len(poss) - 1):
        l1, l2 = get_antinodes(poss[i], poss[i+1:], size_x, size_y)
        antinodes += l1
        antinodes2 += l2


hash = lambda a: str(a[0]) + '|' + str(a[1])

antinodes = set(map(hash, antinodes))
antinodes2 = set(map(hash, antinodes2))
print(len(antinodes))
print(len(antinodes2))
