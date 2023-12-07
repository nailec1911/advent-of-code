#!/usr/bin/python3
f=list(open("input.txt"))

# f=["32T3K 765\n",
# "T55J5 684\n",
# "KK677 28\n",
# "KTJJT 220\n",
# "QQQJA 483\n"]

def value(e):
    c=[0,16,32,64,80,256,1024]
    t=0
    while e:
        d=e.count(e[0])
        if e[0]!='J' and e[0]!='.' and d>1:
            t+=1<<d*2
        e=e.replace(e[0],'')
    return c.index(t)

def test(bid):
    p=value(bid[::])
    if p<6:
        for i in [1]*bid.count('J'):p=p+1+(0<p<4)
        if p>6:p=6

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

ranks=[[] for i in range(9)]
ranks2=[[] for i in range(9)]
for elt in f:
    bid,val=elt.split(' ')
    p=value(bid[::])
    h='AKQJT98765432'
    place(ranks, p, bid, int(val))
    h='AKQT98765432J'
    p=value(bid[::])
    if p<6:
        for i in [1]*bid.count('J'):p=p+1+(0<p<4)
        if p>6:p=6
    place(ranks2, p, bid, int(val))

print("part 1:",get_tot(ranks),"\npart 2:",get_tot(ranks2))
