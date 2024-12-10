
f = [e[:-1] for e in list(open("input.txt"))]

f =  [[int(e) for e in l] for l in f]
len_f = len(f)
len_f0 = len(f[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def get_score_trail(v, i, j):
    if v == 9:
        # f[i][j] = 100 # uncomment this line for part 1
        return 1
    score = 0
    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]
        if not (0 <= ni < len_f and 0 <= nj < len_f0):
            continue
        if f[ni][nj] == v + 1:
            score += get_score_trail(v + 1, ni, nj)
    return score


score = 0
for i in range(len_f):
    for j in range(len_f0):
        if f[i][j] != 0:
            continue
        score +=  get_score_trail(f[i][j], i, j)
        for x in range(len_f):
            f[x] = [9 if e == 100 else e for e in f[x]]

print(score)
