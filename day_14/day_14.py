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
    for i in range(s-1):
        if l[i+1]=='O':
            d=i+1
            while i>=0 and l[i]=='.':i-=1
            if i+1!=d:
                l[i+1]='O'
                l[d]='.'
    return r

def tilt(f):
    res=[]
    for i in range(len(f[0])):
        res.insert(0,[e[i]for e in f])
    return res
# return [list(a) for a in zip(*f)]


def to_north(f):
    for e in f:go_left(e)
    return

def val(f):
    t=0
    l=len(f)
    for i in range(len(f)):
        t+=(l-i)*f[i].count('O')
    return t

def cycle(f):
    for j in range(4):
        f=tilt(f)
        to_north(f)
        f=tilt(f)
        f=tilt(f)
    return f,val(f)

f=[e[:-1] for e in f]
p=tilt(f)
to_north(p)
p=tilt(tilt(tilt(p)))
print('part 1:',val(p))


MEM=[]
values=[]
for i in range(1000000000):
    MEM+=''.join(''.join(e) for e in f),
    f,v=cycle(f)
    values+=v,
    b=''.join(''.join(e) for e in f)
    if b in MEM:
        break

start_patern=MEM.index(b)
pat = len(MEM)-start_patern
rep=(1000000000-start_patern)%pat+start_patern-1
print('part 2:',values[rep])
