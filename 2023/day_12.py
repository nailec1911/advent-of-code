#!/usr/bin/python3
def s(l,n,p,x):
 k=(p,x);r=i=0
 if k in M:return M[k]
 if x>=len(n):
  if'#'in l[p:]:return 0
  return 1
 if p==len(l):return 0
 while l[p+i]in'.?#':
  d=0
  while l[p+i+d]in'?#':d+=1
  if d>=n[x]and'#'!=l[p+i+n[x]]:r+=s(l,n,p+i+n[x]+1,x+1)
  if'#'==l[p+i]:break
  i+=1
 M[k]=r
 return r
a=b=0
for l in list(open('input.txt')):l,n=l.split(' ');n=[int(e) for e in n.split(',')];M={};a+=s(l+' ',n,0,0);M={};b+=s(((l+'?')*5)[:-1]+' ',n*5,0,0)
print("part 1:",a,"\npart 2:",b)
