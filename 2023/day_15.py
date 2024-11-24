#!/usr/bin/python3
def h(val):
 v=0
 for l in val:v=(v+ord(l))*17%256
 return v
d=[{}for i in range(257)];t=0
for e in open('input.txt').read().split(','):
 t+=h(e)
 if'-'in e:l,f=e[:-1],0
 else:l,f=e.split('=')
 b=d[h(l)+1]
 if f:b[l]=int(f)
 elif l in b:b.pop(l)
print("part 1:",t,"\npart 2:",sum(i*v*(j+1)for i in range(257)for j,v in enumerate(d[i].values())))
