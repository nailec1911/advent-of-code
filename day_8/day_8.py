#!/usr/bin/python3

f=list(open('input.txt'))

# f=['RL\n'
# '',
# 'AAA = (BBB, CCC)\n',
# 'BBB = (DDD, EEE)\n',
# 'CCC = (ZZZ, GGG)\n',
# 'DDD = (DDD, DDD)\n',
# 'EEE = (EEE, EEE)\n',
# 'GGG = (GGG, GGG)\n',
# 'ZZZ = (ZZZ, ZZZ)\n']

# f=['LLR\n','',
# 'AAA = (BBB, BBB)\n',
# 'BBB = (AAA, ZZZ)\n',
# 'ZZZ = (ZZZ, ZZZ)\n']

# f=['LR\n','',
# '11A = (11B, XXX)\n',
# '11B = (XXX, 11Z)\n',
# '11Z = (11B, XXX)\n',
# '22A = (22B, XXX)\n',
# '22B = (22C, 22C)\n',
# '22C = (22Z, 22Z)\n',
# '22Z = (22B, 22B)\n',
# 'XXX = (XXX, XXX)\n']

# f=list(f)

def next(path,c):
    if n=='R':return c[1]
    return c[0]


path=list(f.pop(0)[:-1])
f.pop(0)
f=[[e[:3],e[7:10],e[12:-2]] for e in f]
d={}

for n in f:
    d[n[0]]=(n[1],n[2])

c='AAA'
p=path[::]
t=0
while c!='ZZZ':
    n=p.pop(0)
    p+=n,
    c=next(p,d[c])
    t+=1
print(t)

def end(l):
    for e in l:
        if e[2]!='Z':return 1
    return 0

from math import gcd
def res(l):
    #This only work if each x round, we fall back on the same node ending with Z
    # it works, but How can we be sure of that ???
    smallest_multiple = 1
    for v in l:
        smallest_multiple = (v*smallest_multiple)//gcd(v,smallest_multiple)
    print(smallest_multiple)
    exit()

c=[e for e in d if e[2]=='A']
t=0
T={}
while True:
    n=path.pop(0)
    path+=n,
    for i in range(len(c)):
        c[i]=next(path,d[c[i]])
        if c[i][2]=='Z':
            T[i]=t+1
        if len(T)==len(c):res(T.values())
    t+=1


# print("part 1:",r,"\npart 2:",r)
