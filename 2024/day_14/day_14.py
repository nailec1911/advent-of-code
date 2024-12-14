import re

f = [e[:-1] for e in list(open("input.txt"))]
SIZE_Y = 103
SIZE_X = 101

MID_X = int((SIZE_X - 1) / 2)
MID_Y = int((SIZE_Y - 1) / 2)

f = [[int(x) for x in re.findall(r'-?\d+', e)] for e in f]

quads = []
for i in range(10000):
    quadrants = [0, 0, 0, 0]
    for e in f:
        px, py, vx, vy = e
        px = (px + vx * i) % SIZE_X
        py = (py + vy * i) % SIZE_Y
        if px == MID_X or py == MID_Y:
            continue
        quadrants[(px < MID_X) + (py < MID_Y) * 2] += 1
    print(i)
    quads.append(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

print(quads[100])
print(quads.index(min(quads)))
