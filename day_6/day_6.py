#!/usr/bin/python3
f=open("input.txt","r").read().split('\n')
a,b=[],[]
for i in 0,1:
    f[i]=f[i].split(':')[1].split(' ')
    a+=[int(e)for e in f[i]if e],
    b+=int(''.join(f[i])),

def dist(t,d):return d*(t-d)

def first(time,r):
    for i in range(time):
        if dist(time,i)>r:
            return i
    return 0

def last(time,r):
    for i in range(time,-1,-1):
        if dist(time,i)>r:
            return i
    return 0

s=1
for i in range(len(a[0])):
    s*=last(a[0][i],a[1][i])-first(a[0][i],a[1][i])+1
print("part 1:",s,"\npart 2:",last(b[0],b[1])-first(b[0],b[1])+1)
