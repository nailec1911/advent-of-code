f = [[e[0], int(e[1:-1])] for e in list(open("input.txt"))]
pos, res1, res2 = 50, 0, 0
for direc, val in f:
    rem = val % 100
    pos += (rem if direc == 'R' else -rem)
    res2 += int(val / 100) + (pos != -rem and not 0 < pos < 100)
    res1 += (pos := pos % 100) == 0
print(res1, res2)


# First version to get the solution fast
# for direc, val in f:
#     for i in range(val):
#         pos += 1 if direc == 'R' else -1
#         pos = pos % 100
#         if pos == 0:
#             res2 += 1
#     if pos == 0:
#         res1 += 1
