#!/usr/bin/python3
f=[list(e[:-1])for e in list(open('input.txt'))]
m,l=len(f),len(f[0])
def v(c,r):
 t=0
 for k in range(m*l):
  if'#'==f[k//l][k%l]:t+=r[k//l]-r[i]+abs(c[k%l]-c[j])
 return t
r=[]
c=[]
rl=[]
cl=[]
q=u=0
for i in range(m):
 if{*f[i]}=={'.'}:q+=1
 r+=i+q*1,;rl+=i+q*999999,
for i in range(l):
 if{e[i]for e in f}=={'.'}:u+=1
 c+=i+u*1,;cl+=i+u*999999,
x=y=0
for i in range(m*l):
 i,j=i//l,i%l
 if'#'==f[i][j]:f[i][j]='.';x+=v(c,r);y+=v(cl,rl)
print("part 1:",x,"\npart 2:",y)
