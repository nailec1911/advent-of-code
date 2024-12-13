def get_min(objective, a, b):
    res = []

    for qa in range(objective // a + 1):
        remainder = objective - a * qa
        if remainder % b != 0:
            continue
        qb = remainder // b
        res.append((qa, qb))
    return res


def get_min2(objx, xa, xb, objy, ya, yb):
    qb = round((objy * xa - objx * ya) / (xa * yb - ya * xb))
    qa = round((objx - qb * xb) / xa)
    if qa * xa + qb * xb == objx and qa * ya + qb * yb == objy:
        return (qa, qb)
    return (0, 0)


#   objx = a * xa + b * xb
#   objy = a * ya + b * yb
#
#   objx * ya = (a * xa + b * xb) * ya
#   objy * xa = (a * ya + b * yb) * xa
#
#   objy * xa - objx * ya = (a * ya + b * yb) * xa - (a * xa + b * xb) * ya
#                     = xa * a * ya + xa * b * yb - ya * a * xa - ya * b * xb
#                     = xa * b * yb - ya * b * xb
#   objx * xa - objy * ya = b * (xa * yb - ya * xb)
#
#   b = (objy * xa - objx * ya) / (xa * yb - ya * xb)
#
#   a = (objx - b * xb) / xa

f = [e[:-1] for e in list(open("input.txt"))]
score = 0
score2 = 0
for i in range(0, len(f), 4):
    xa = int(f[i][12:14])
    ya = int(f[i][17:])

    xb = int(f[i + 1][12:14])
    yb = int(f[i + 1][17:])

    p = f[i + 2].split('=')
    x = int(p[1][:-3])
    y = int(p[2])

    # qx = get_min(x, xa, xb)
    # qy = get_min(y, ya, yb)
    # if not qx or not qy:
    # continue
    # q = list(set(qx) & set(qy))
    # if not q:
    # continue
    # q.sort(key=lambda x: x[0])
    q = get_min2(x, xa, xb, y, ya, yb)
    score += q[0] * 3 + q[1]
    q = get_min2(x + 10000000000000, xa, xb, y + 10000000000000, ya, yb)
    score2 += q[0] * 3 + q[1]

print(score, score2)
