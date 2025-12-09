f = [
[7,1],
[11,1],
[11,7],
[9,7],
[9,5],
[2,5],
[2,3],
[7,3],
]

f = [[int(x) for x in e[:-1].split(',')] for e in list(open("input.txt"))]

def segment_in(p1, p2, xmin, xmax, ymin, ymax):
    (x1, y1) = p1
    (x2, y2) = p2

    if x1 <= xmin and x2 <= xmin: return False
    if x1 >= xmax and x2 >= xmax: return False
    if y1 <= ymin and y2 <= ymin: return False
    if y1 >= ymax and y2 >= ymax: return False
    return True


res = 0
res2 = 0
for i in range(len(f) - 1):
    for j in range(i + 1, len(f)):
        a, b = f[i]
        c, d = f[j]
        dim = (abs(a - c) + 1) * (abs(b - d) + 1)
        if dim > res:
            res = dim
        possible = True

        if dim > res2:
            xmin = min(a, c)
            xmax = max(a, c)
            ymin = min(b, d)
            ymax = max(b, d)
            for z in range(len(f)):
                p1, p2 = f[z], f[(z+1) % len(f)]
                if segment_in(p1, p2, xmin, xmax, ymin, ymax):
                    possible = False
                    break
            if possible:
                res2 = dim

print(res)
print(res2)
