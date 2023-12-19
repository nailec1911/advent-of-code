#!/usr/bin/python3

works,part_list=open("input.txt").read()[:-1].split('\n\n')
workflows={}
for w in works.split('\n'):
    name,conds=w.split('{')
    workflows[name]=[e.split(':')for e in conds[:-1].split(',')]


a={'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}
w='in'
queue=[['in',a]]
u=[]
while queue:
    w,vals=queue.pop(0)
    if w=='R':continue
    if w=='A':
        u+=list(vals.values()),
        continue
    for v1,v2 in vals.values():
        if v2<v1:continue

    conds=workflows[w]
    for c,r in conds[:-1]:
        x=c[0]
        old=vals[x]
        new={k:i for k,i in vals.items()}
        if c[1]=='>':
            new[x]=(int(c[2:])+1,old[1])
            vals[x]=(old[0],int(c[2:]))
        else:
            new[x]=(old[0],int(c[2:])-1)
            vals[x]=(int(c[2:]),old[1])
        queue.append([r,new])
    queue.append([conds[-1][0],vals])

r=sum(v[0]*v[1]*v[2]*v[3] for v in [[1+e[1]-e[0]for e in vals]for vals in u])


t=[r for r in [[int(p[2:])for p in e[1:-1].split(',')]for e in part_list.split('\n')]for v in u if all(v[i][0]<=r[i]<=v[i][1]for i in(0,1,2,3))]
print("part 1:",sum(sum(t,[])),"\npart 2:",r)
