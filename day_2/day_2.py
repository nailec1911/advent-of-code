#!/usr/bin/python3
e={'r':0,'g':1,'b':2}
t,p,i=0,0,1
for l in open("input.txt", "r").read().split('\n'):
 a,r=[0,0,0],True
 for c in l.split(':')[1].replace(',',';').split(';'):
  j=0
  while not c[j]in'rgb':j+=1
  n,j=int(c[:j]),e[c[j]]
  if n>a[j]:a[j]=n
  if n>12+j:r=False
 if r:t+=i
 i+=1
 p+=a[0]*a[1]*a[2]
print("part 1:",t)
print("part 2:",p)
