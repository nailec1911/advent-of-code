
f = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  ",
]
f = [e[:-1] for e in list(open("input.txt"))]


def ops(sign, nbs):
    res = nbs[0]
    for e in nbs[1:]:
        if e == 0:
            continue
        if sign == '*':
            res *= e
        else:
            res += e
    return res


signs = f.pop(-1)
count = 0
res = 0
for i in range(len(signs) - 1, -1, -1):
    count += 1
    if signs[i] != ' ':
        nbs = []
        for j in range(count):
            nb = 0
            for e in f:
                if e[i + j] == ' ':
                    continue
                nb = nb * 10 + int(e[i + j])
            nbs.append(nb)
        a = ops(signs[i], nbs)
        res += a
        count = 0
print(res)











# for i in range(len(f)):
    # f[i] = f[i].split(' ')
    # while '' in f[i]:
        # f[i].remove('')
#
# signs = f.pop(-1)
# res = 0
# for i, sign in enumerate(signs):
    # nbs = 0
    # temp = int(f[0][i])
    # for e in f[1:]:
        # if sign == '*':
            # temp *= int(e[i])
        # if sign == '+':
            # temp += int(e[i])
    # res += temp
# print(res)
