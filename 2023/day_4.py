#!/usr/bin/python3
f=open("input.txt","r").readlines()
t=i=0
d=[1]*len(f)
for e in f:
 c=38-len(set(e[e.index(':'):-1].split(' ')))
 t+=2**(c-1)//1
 while c:d[i+c]+=d[i];c-=1
 i+=1
print("part 1:",t,"\npart 2:",sum(d))
