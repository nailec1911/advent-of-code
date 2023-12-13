#!/usr/bin/python3
t,u=[sum([i*q for p in[e.split()for e in open('input.txt').read()[:-1].split('\n\n')]for d,q in[[p,1],[[*zip(*p)],100]]for i in range(len(d[0]))if sum(sum(a!=b for a,b in zip(l[:i][::-1],l[i:]))for l in d)==k])for k in(0,1)]
print("part 1:",t,"\npart 2:",u)
