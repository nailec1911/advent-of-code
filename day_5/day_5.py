#!/usr/bin/python3
def t(l,c):
 for z in l[::]:
  a,b=l.pop(0);r=[a,b],
  for e,f,g in c:
   y,z=max(a,f),min(b,f+g)
   if y<z:
    r=[y-f+e,z-f+e],
    if a<y:r+=[a,y],
    if z<b:r+=[z,b],
    break
  l+=r
f=list(open("input.txt"))
s=[[int(e),int(e)+1]for e in f.pop(0)[7:].split()]
l=[[a[0],a[0]+b[0]]for a,b in zip(s,s[1:])][::2]
while f:
 f=f[2:];c=[]
 while f and f[0]!="\n":c+=[int(e)for e in f.pop(0).split()],
 t(s,c);t(l,c)
print("part 1:",min(s)[0],"\npart 2:",min(l)[0])
