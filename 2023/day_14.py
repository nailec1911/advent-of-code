#!/usr/bin/python3
r=range;l=len
n=lambda f:[*zip(*['#'.join(''.join(reversed(sorted(e)))for e in''.join(k).split('#'))for k in[*zip(*f)]])]
c=lambda f:sum([f[i].count('O')*(l(f)-i)for i in r(l(f))])
def cycle(f):
 for z in[1]*4:f=n(f);f=[[f[l(f)-j-1][i]for j in r(l(f))]for i in r(l(f[0]))]
 return f
f=[e[:-1]for e in open("input.txt")]
t=c(n(f))
M=[]
v=[]
while((b:=[e[::]for e in f])in M)<1:M+=b,;f=cycle(f);v+=c(f),
s=M.index(b)
print("part 1:",t,"\npart 2:",v[(10**9-s)%(l(M)-s)+s-1])
