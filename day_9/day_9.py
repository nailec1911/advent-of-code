#!/usr/bin/python3
f=list(open('input.txt'))

# f=["0 3 6 9 12 15\n","1 3 6 10 15 21\n","10 13 16 21 30 45\n"]

def conv(l):
    return [int(e)for e in l.split()]

def hist(l):
    end=[l[-1]]
    first=[l[0]]
    while set(l)!={0}:
        r=[]
        for i in range(len(l)-1):
            r+=[l[i+1]-l[i]]
        end=[r[-1]]+end
        first=[r[0]]+first

        l=r
    r=0
    for e in end:r+=e
    z=0
    for e in first:z=e-z
    return r,z

f=map(conv,f)
t=0
u=0
for l in f:
    a,b=hist(l)
    t+=a
    u+=b
print("part 1:",t,"\npart 2:",u)
