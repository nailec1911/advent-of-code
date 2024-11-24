#!/usr/bin/python3
a={'R':(0,1),'L':(0,-1),'D':(1,0),'U':(-1,0)}
def q(l,x,y,p,r,z):
 j=l.split(' ');m,n,o=*a[j[0]],int(j[1])
 if z:m,n,o=*a[{'0':'R','2':'L','1':'D','3':'U'}[l[-3]]],int(l[-8:-3],16)
 m*=o;n*=o
 return x+m,y+n,p+o,r+y*m
c=d=e=f=g=h=i=j=0
for l in list(open("input.txt")):c,d,e,f=q(l,c,d,e,f,0);g,h,i,j=q(l,g,h,i,j,1)
print("part 1:",f+e//2+1,"\npart 2:",j+i//2+1)
