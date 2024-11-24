#!/usr/bin/python3
def v(e,p):
 r=0;j=e.count('J')
 while e:
  c=e[0];d=e.count(c)
  if p|(c!='J'):r+=d-(d<3)+(d>3)
  e=e.replace(c,'')
 if~-p&(r<6):
  for _ in[1]*j:r=r+1+(0<r<4)
  if r>6:r=6
 return r
def r(l,j):
 if~-j:t['J']='0'
 l.sort(key=lambda e:[v(e[0],j),*[t.get(c,c)for c in e[0]]])
 return sum([int(e[1])*(i+1)for i,e in enumerate(l)])
f=[e.split()for e in list(open("input.txt"))]
t={'A':'E','K':'D','Q':'C','J':'B','T':'A'}
print("part 1:",r(f[::],1),"\npart 2:",r(f,0))
