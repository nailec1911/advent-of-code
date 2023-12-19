#!/usr/bin/python3
f=open("input.txt").read()[:-1]

# f="px{a<2006:qkq,m>2090:A,rfg}\n\
# pv{a>1716:R,A}\n\
# lnx{m>1548:A,A}\n\
# rfg{s<537:gd,x>2440:R,A}\n\
# qs{s>3448:A,lnx}\n\
# qkq{x<1416:A,crn}\n\
# crn{x>2662:A,R}\n\
# in{s<1351:px,qqz}\n\
# qqz{s>2770:qs,m<1801:hdj,R}\n\
# gd{a>3333:R,R}\n\
# hdj{m>838:A,pv}\n\
# \n\
# {x=787,m=2655,a=1222,s=2876}\n\
# {x=1679,m=44,a=2067,s=496}\n\
# {x=2036,m=264,a=79,s=2244}\n\
# {x=2461,m=1339,a=466,s=291}\n\
# {x=2127,m=1623,a=2188,s=1013}"

p1,p2=f.split('\n\n')
workflows={}
a=2
tree={}
for w in p1.split('\n'):
    name,conds=w.split('{')
    conds=conds[:-1].split(',')
    obj=len(conds)
    for i in range(len(conds)):conds[i]=conds[i].split(':')
    s=[f"'{c[1]}' if {c[0]} else "for c in conds[:-1]]
    workflows[name]=''.join(s)+"'"+conds[-1][0]+"'",conds


t=0
for part in p2.split('\n'):
    d={'x':0,'m':0,'a':0,'s':0}
    part=part[1:-1].split(',')
    for p in part:
        d[p[0]]=int(p[2:])
    x,m,a,s=d.values()
    w='in'
    while not w in 'RA':
        w=eval(workflows[w][0])
    if w=='A':t+=x+m+a+s


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
    conds=workflows[w][1]
    for c,r in conds[:-1]:
        old=vals[c[0]]
        new={k:i for k,i in vals.items()}
        if c[1]=='>':
            new[c[0]]=(int(c[2:])+1,old[1])
            vals[c[0]]=(old[0],int(c[2:]))
        else:
            new[c[0]]=(old[0],int(c[2:])-1)
            vals[c[0]]=(int(c[2:]),old[1])
        queue.append([r,new])
    queue.append([conds[-1][0],vals])

r=sum(v[0]*v[1]*v[2]*v[3] for v in [[1+e[1]-e[0]for e in vals]for vals in u])
print("part 1:",t,"\npart 2:",r)
