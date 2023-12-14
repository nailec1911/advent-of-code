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

def north(f):
    f=[*zip(*f)]
    for i in range(len(f)):
        f[i]='#'.join(map(lambda e:''.join(reversed(sorted(e))),''.join(f[i]).split('#')))
    return [*zip(*f)]

def val(f):
   l=len(f)
   return sum([f[i].count('O')*(l-i) for i in range(l)])
# print('#'.join(map(lambda e:''.join(reversed(sorted(e))), s.split('#'))))

def rot(f):
    return [[f[j][i] for j in range(len(f)-1,-1,-1)] for i in range(len(f[0]))]

def cycle(f):
    for i in 1,2,3,4:
        f=north(f)
        f=rot(f)
    return f,val(f)

f=[e[:-1] for e in f]

print('part 1:',val(north(f)))

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
