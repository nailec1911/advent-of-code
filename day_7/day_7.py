#!/usr/bin/python3
f=map(list,list(open("input.txt")))

f=["32T3K 765\n",
"T55J5 684\n",
"KK677 28\n",
"KTJJT 220\n",
"QQQJA 483\n"]

def value(e,p):
 t=0
 j=e.count('J')
 while e:
  d=e.count(e[0])
  if p or e[0]!='J':t+=d-(d<3)+(d>3)
  e=e.replace(e[0],'')
 if not p and t<6:
  for i in [1]*j:t=t+1+(0<t<4)
  if t>6:t=6
 return t

def conv(e):
 h,b=e.split(' ')
 return h,b

def s(c): return list(L).index(c)
def compare(a,b):
 i=0
 while a[i]==b[i]:i+=1
 return s(a[i])>s(b[i])

def get_tot(r):
 t=0
 i=1
 for g in r:
  for h,z in g:t+=h*i;i+=1
 return t


def sor(e):
 return value(e[0],j),*[tr.get(c,c) for c in e[0]]


l=list(map(conv, f))
m=l[::]
j=1
tr={'A':'E','K':'D','Q':'C','J':'B','T':'A'}
l.sort(key=sor)
print(l)
tr['J']='0'
j=0
m.sort(key=sor)
print(m)
exit()




def res(p):
 r=[[] for i in [1]*8]
 for h,b,*k in l:
  i=0
  while i<len(r[k[p]]) and compare(r[k[p]][i][1],h): i+=1
  r[k[p]].insert(i,[int(b),h])
 return get_tot(r)
L='AKQJT98765432'
l=list(map(conv, f))
print(res(0))
L='AKQT98765432J'
r=[[] for i in [1]*8]
print(res(1))

exit()
def value(e,p):
 t=0
 while e:
  d=e.count(e[0])
  if p or e[0]!='J':t+=d-(d<3)+(d>3)
  e=e.replace(e[0],'')
 return t

def s(c): return list(h).index(c)
def compare(a,b):
 i=0
 while a[i]==b[i]:i+=1
 return s(a[i])>s(b[i])
def place(r, pos, bid,v):
 i=0
 while i<len(r[pos]) and compare(r[pos][i][0],bid): i+=1
 r[pos].insert(i,[bid,v])

def get_tot(r):
 t=0
 i=1
 for g in r:
  for h in g:
   t+=h[1]*i
   i+=1
 return t

def res(q):
 r=[[] for i in range(9)]
 for elt in f:
  bid,val=elt.split(' ')
  p=value(bid[::],q)
  if p<6:
   for i in [1]*bid.count('J'):p=p+1+(0<p<4)
   if p>6:p=6
  place(r, p, bid, int(val))
 return get_tot(r)

h='AKQJT98765432'
print(res(1))
h='AKQT98765432J'
print(res(0))


exit()
ranks=[[] for i in range(9)]
ranks2=[[] for i in range(9)]
for elt in f:
 bid,val=elt.split(' ')
 p=value(bid[::])
 h='AKQJT98765432'
 place(ranks, p, bid, int(val))
 h='AKQT98765432J'
 p=value(bid[::])
 if p<6:
  for i in [1]*bid.count('J'):p=p+1+(0<p<4)
  if p>6:p=6
 place(ranks2, p, bid, int(val))

print("part 1:",get_tot(ranks),"\npart 2:",get_tot(ranks2))
