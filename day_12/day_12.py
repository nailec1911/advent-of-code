#!/usr/bin/python3
f=list(open('input.txt'))

# f=[
# "???.### 1,1,3\n",
# ".??..??...?##. 1,1,3\n",
# "?#?#?#?#?#?#?#? 1,3,1,6\n",
# "????.#...#... 4,1,1\n",
# "????.######..#####. 1,6,5\n",
# "?###???????? 3,2,1\n"]

def possibilities(l,n,li,ni):
    k=(li,ni)
    if k in MEM: return MEM[k]
    r=0
    if ni>=len(n):
        if '#'in l[li:]: return 0
        return 1
    if li==len(l):return 0
    i=0
    while l[li+i]in '.?#':
        d=0
        while l[li+i+d]in'?#':d+=1
        if d>=n[ni] and l[li+i+n[ni]]!='#':
            r+=possibilities(l,n,li+i+n[ni]+1,ni+1)
        if l[li+i]=='#':break
        if len(l[li:])-1<sum(n[ni:])+len(n[ni:]):break
        i+=1
    MEM[k]=r
    return r

t1=t2=0
for i in range(len(f)):
    l,n=f[i].split(' ')
    n=[int(e) for e in n.split(',')]
    MEM={}
    t1+=possibilities(l+' ',n,0,0)
    MEM={}
    t2+=possibilities(((l+'?')*5)[:-1]+' ',n*5,0,0)

print(t1,t2)


# print("part 1:",x,"\npart 2:",y)
