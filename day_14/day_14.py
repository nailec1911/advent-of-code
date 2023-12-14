#!/usr/bin/python3
f=list(open("input.txt"))
# print(f)
# f=[
# 'O....#....\n',
# 'O.OO#....#\n',
# '.....##...\n',
# 'OO.#O....O\n',
# '.O.....O#.\n',
# 'O.#..O.#.#\n',
# '..O..#O..O\n',
# '.......O..\n',
# '#....###..\n',
# '#OO..#....\n',
# ]

def go_left(l):
    r=0
    s=len(l)
    # print(l)
    for i in range(s-1):
        if l[i+1]=='O':
            d=i+1
            while i>=0 and l[i]=='.':i-=1
            if i+1!=d:
                l[i+1]='O'
                l[d]='.'
    for i in range(s):
        if l[i]=='O':r+=s-i
    return r

def tilt(f):
    res=[]
    for i in range(len(f[0])):
        res.insert(0,[e[i]for e in f])
    return res
# return [list(a) for a in zip(*f)]


def val(f):
    t=0
    for e in f:t+=go_left(e)
    return t


def cycle(f):
    for j in range(4):
        f=tilt(f)
        # for e in f:print(''.join(e))
        u=val(f)
        f=tilt(f)
        f=tilt(f)
        # print()
    return f,u

f=[e[:-1] for e in f]
t=val(tilt(f))
print('part 1:',t)
MEM=[]
u=0
for i in range(1000000000):
    # print(i)
    a=''.join(''.join(e) for e in f)
    MEM+=a,
    f,u=cycle(f)
    # for e in f:print(''.join(e))
    # print()
    if ''.join(''.join(e) for e in f) in MEM:
        break
    # if a==''.join(''.join(e) for e in f):
        # break

print(i)
print(1000000000%i)
for i in range(1000000000%i):
    f,u=cycle(f)
# for e in f:print(''.join(e))
print('part 2:',u)
