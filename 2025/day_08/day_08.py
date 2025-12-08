from math import sqrt

f = [
[162,817,812],
[57,618,57],
[906,360,560],
[592,479,940],
[352,342,300],
[466,668,158],
[542,29,236],
[431,825,988],
[739,650,466],
[52,470,668],
[216,146,977],
[819,987,18],
[117,168,530],
[805,96,715],
[346,949,466],
[970,615,88],
[941,993,340],
[862,61,35],
[984,92,344],
[425,690,689],
]

f = [[int(x) for x in e[:-1].split(',')] for e in list(open("input.txt"))]


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 +(a[2] - b[2]) ** 2)

def find_connected(x, y, connected):
    sx, sy = -1, -1
    for i, c in enumerate(connected):
        if x in c:
            sx = i
        if y in c:
            sy = i
    return sx, sy


edges = {}
for i, box in enumerate(f):
    for j in range(i + 1, len(f)):
        d = distance(box, f[j])
        edges[(i, j)] = d


edges = sorted(edges.items(), key=lambda e: e[1])

connected :list[set] = []

done = set()
aa = 0
for (x, y), d in edges:
    if aa == 1000:
        sizes = sorted([len(e) for e in connected], reverse=True)
        part1 = sizes[0] * sizes[1] * sizes[2]
    aa += 1

    sx, sy = find_connected(x, y, connected)
    if sx == -1 and sy == -1:
        connected.append(set([x, y]))
    if sx == -1 and sy != -1:
        connected[sy].add(x)
    if sy == -1 and sx != -1:
        connected[sx].add(y)
    if sy != -1 and sx != -1 and sx != sy:
        connected[sx] |= connected[sy]
        connected.pop(sy)
    done.add(x)
    done.add(y)
    if len(done) == 1000:
        part2 = f[x][0] * f[y][0]
        break

print(part1)
print(part2)
