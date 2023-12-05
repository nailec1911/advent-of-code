#!/usr/bin/python3
f=open("input.txt","r").read().split('\n')
def g(f,l,r=''):
 while f[l].isdigit():l-=1
 while f[(l:=l+1)].isdigit():r+=f[l];f[l]='.'
 return int(r)
t=r=0
l=len(f[0])
f+='.'*l,
f=[list(e+'.')for e in f]
z=len(f)
for k in range(z*l):
 i,j=k//z,k%l
 if(f[i][j]in'.0123456789')-1:
  n=[g(f[i+x],j+y)for x,y in[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]if f[i+x][j+y].isdigit()];t+=sum(n)
  if len(n)==2:r+=n[0]*n[1]
print("part 1:",t,"\npart 2:",r)
