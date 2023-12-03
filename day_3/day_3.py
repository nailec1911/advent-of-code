#!/usr/bin/python3

f = open("input.txt", "r").readlines()

# f= ["467..114..\n",
    # "...*......\n",
    # "..35..633.\n",
    # "......#...\n",
    # "617*......\n",
    # ".....+.58.\n",
    # "..592.....\n",
    # "......755.\n",
    # "...$.*....\n",
    # ".664.598..\n"]


def get_nb(f, i, j):
    while f[i][j].isdigit():
        j -= 1
    l=1
    nb=0
    while f[i][j+l].isdigit():
        nb=nb*10+int(f[i][j+l])
        l += 1
    return nb, l-1

def check_char(f, i, j, l):
    if len(set(f[i][j+l] + f[i][j-1] + f[i-1][j-1:j+l+1] + f[i+1][j-1:j+l+1]))-1:
        return True
    return False

for i in range(len(f)):
    f[i]='.'+f[i][:-1]+'.'
f.append('.'*len(f[0]))
f.insert(0, '.'*len(f[0]))

t = 0
for i in range(len(f)):
    l = 0
    for j in range(len(f[i])):
        if l!=0:
            l-=1
            continue
        if f[i][j].isdigit():
            nb, l = get_nb(f, i, j)
            if check_char(f, i, j, l):
                t+= nb

print("part 1:", t)


def gear_ratio(f, i, j):
    inds = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
    r = [f[ind[0]][ind[1]] for ind in inds]
    if r[1].isdigit():
        if r[2].isdigit(): r.pop(2), inds.pop(2)
        if r[0].isdigit(): r.pop(0), inds.pop(0)
    if r[-2].isdigit():
        if r[-3].isdigit(): r.pop(-3), inds.pop(-3)
        if r[-1].isdigit(): r.pop(-1), inds.pop(-1)
    c = 0
    nb = 1
    for i in range(len(r)):
        if r[i].isdigit():
            c += 1
            nb *= get_nb(f, *inds[i])[0]
    if c != 2: return 0
    return nb

t=0
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j]=='*':
            t += gear_ratio(f, i, j)

print("part 2:", t)
