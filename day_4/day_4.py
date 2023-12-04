#!/usr/bin/python3

f = open("input.txt", "r").read().split('\n')

def nbs(l):
    return [int(v) for v in l.split(' ') if v!='']

def value(card):
    w,y=card.split('|')
    w,y=nbs(w),nbs(y)

    t=0
    n=0
    for v in w:
        if v in y:
            n+=1
            if t==0:t=1
            else: t*=2
    return t,n

t=0
d=[1]*len(f)
for i in range(len(f)):
    card=f[i].split(':')[1]
    z,c=value(card)
    t+=z
    for j in range(c):
        d[i+1+j]+=d[i]
print("part 1:",t)
print("part 2:",sum(d))

