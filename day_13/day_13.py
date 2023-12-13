#!/usr/bin/python3
f=[e.split('\n') for e in open('input.txt').read()[:-1].split('\n\n')]

def check_hor(pat,i):
    j=0
    while i+j+1<len(pat) and i-j>=0:
        if pat[i+j+1]!=pat[i-j]:
            return False
        j+=1
    return True

def hor(pat):
    return [i+1 for i in range(len(pat)-1) if check_hor(pat,i)]

def value(pat):
    return [e*100 for e in hor(pat)]+hor([*zip(*pat)])

t=u=0
for e in f:
    e=[list(v)for v in e]
    v=value(e)[0]

    i=0
    s=True
    while i<len(e)and s:
        j=0
        while j<len(e[0])and s:
            c=e[i][j]
            if c=='#':e[i][j]='.'
            else:e[i][j]='#'
            for v2 in value(e):
                if v2!=v:s=False;break
            e[i][j]=c
            j+=1
        i+=1
    t+=v
    u+=v2

print("part 1:",t,"\npart 2:",u)
