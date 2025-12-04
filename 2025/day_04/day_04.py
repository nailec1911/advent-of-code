f = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@.",
]

f = [e[:-1] for e in list(open("input.txt"))]

f.insert(0, '.' * len(f[0]))
f.append('.' * len(f[0]))

for i in range(len(f)):
    f[i] = list('.' + f[i] + '.')


rm = True
res = 0
res2 = 0
while rm:
    rm = False
    to_remove = []
    for i in range(1, len(f) - 1):
        for j in range(1, len(f[0]) - 1):
            if f[i][j] != '@':
                continue
            around = f[i - 1][j-1:j+2] + f[i][j - 1:j + 2] + f[i + 1][j - 1:j + 2]
            if around.count('@') <= 4:
                res2 += 1
                to_remove.append([i, j])
                rm = True
    if res == 0:
        res += res2
    for i, j in to_remove:
        f[i][j] = 'X'

print(res)
print(res2)
