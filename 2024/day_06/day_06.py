f = [e[:-1] for e in list(open("input.txt"))]

dirs = [(-1, 0),(0, 1), (1, 0), (0, -1)]
start = [0, 0]
soldat = '^>v<'
dir = []

for i, line in enumerate(f):
    for j, c in enumerate(line):
        if (c in soldat):
            start = [i, j]
            dir = soldat.index(c)
            break
    if start != [0, 0]:
        break


def turn(f, start, dir):
    i,j = start
    t = True
    while 0 <= i < len(f) and 0 <= j < len(f[0]) and t:
        if type(f[i][j]) != list:
            f[i][j] = []
        f[i][j].append(soldat[dir])

        d1, d2 = dirs[dir]
        if not (0 <= i + d1 < len(f) and 0 <= j + d2 < len(f[0])):
            break
        while f[i + d1][j + d2] == '#':
            dir = (dir + 1) % 4
            d1, d2 = dirs[dir]
        i += dirs[dir][0]
        j += dirs[dir][1]

        if type(f[i][j]) == list and soldat[dir] in f[i][j]:
            t = False

    for i in range(len(f)):
        f[i] = [x[0] if type(x) == list else x  for x in f[i]]
    return t



f = [list(e) for e in f]

score2 = 0
cp = [e[::] for e in f]
turn(cp, start, dir)


test = [e[::] for e in f]
a, b = len(f), len(f[0])
for m in range(a):
    for n in range(b):
        if cp[m][n] not in soldat:
            continue
        test[m][n] = '#'

        t = turn(test, start, dir)
        print(a, b, '|', m, n)
        if not t:
            score2 += 1

        test[m][n] = '.'

cp = [''.join(e) for e in cp]
cp = ''.join(cp)

score = sum([cp.count(d) for d in soldat])
print(score, score2)
