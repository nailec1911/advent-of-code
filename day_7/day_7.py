#!/usr/bin/python3
f=list(open("input.txt"))

f=["32T3K 765\n",
"T55J5 684\n",
"KK677 28\n",
"KTJJT 220\n",
"QQQJA 483\n"]

def value(e,p):
    t=0
    while e:
        d=e.count(e[0])
        if p: d+=e.count('J')
        if d>1:
            t+=(d-1)/2+(d>2)+(d>3)
        e=e.replace(e[0],'')
    print(t)
    return int(t*2)

def s(c): return list(h).index(c)
def compare(a,b):
    i=0
    while a[i]==b[i]:i+=1
    return s(a[i])>s(b[i])
def place(r, pos, bid,v):
    i=0
    while i<len(r[pos]) and compare(r[pos][i][0],bid): i+=1
    r[pos].insert(i,[bid,v])

def get_tot(r):
    t=0
    i=1
    for g in r:
        for h in g:
            t+=h[1]*i
            i+=1
    return t

ranks=[[] for i in range(30)]
ranks2=[[] for i in range(30)]
for elt in f:
    print(elt)
    bid,val=elt[:-1].split()
    p=value(bid[::],0)
    h='AKQJT98765432'
    place(ranks, p, bid, int(val))
    # h='AKQT98765432J'
    # p=value(bid[::],1)
    # print(p)
    # place(ranks2, p, bid, int(val))

print('\n\nend',ranks2)
print(get_tot(ranks),get_tot(ranks2))
