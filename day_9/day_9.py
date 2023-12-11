#!/usr/bin/python3
def h(l):
 end=[l[-1]];first=[l[0]]
 while{*l}!={0}:
  r=[]
  for i in range(len(l)-1):r+=[l[i+1]-l[i]]
  end=[r[-1]]+end;first=[r[0]]+first;l=r
 r=z=0
 for e in end:r+=e
 for e in first:z=e-z
 return r,z
f=map(lambda l:[int(e)for e in l.split()],list(open('input.txt')))
t=u=0
for l in f:a,b=h(l);t+=a;u+=b
print("part 1:",t,"\npart 2:",u)
