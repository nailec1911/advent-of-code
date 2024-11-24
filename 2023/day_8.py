#!/usr/bin/python3
f=list(open('input.txt'))
p=list(f[0][:-1])
d={e[:3]:(e[7:10],e[12:-2])for e in f[2:]}
g=lambda a,b:b and g(b,a%b)or a
def c(l):
 s=1
 for v in l:s=(v*s)//g(v,s)
 return s
def r(l):
 t=0;T={}
 while len(l)>1 or l[0]!='ZZZ':
  for i in range(len(l)):
   l[i]=d[l[i]][0]if'L'==p[t%len(p)]else d[l[i]][1]
   if len(l)<2:break
   if'Z'==l[i][2]:T[i]=t+1
   if len(T)==len(l):return c(T.values())
  t+=1
 return t
print("part 1:",r(['AAA']),"\npart 2:",r([e for e in d if e[2]=='A']))
