#!/usr/bin/python3
f=[e.split('\n') for e in open('input.txt').read()[:-1].split('\n\n')]


a=[
'#.##..##.',
'..#.##.#.',
'##......#',
'##......#',
'..#.##.#.',
'..##..##.',
'#.#.##.#.']

b=[
'#...##..#',
'#....#..#',
'..##..###',
'#####.##.',
'#####.##.',
'..##..###',
'#....#..#']

def check_hor(pat,i):
    j=0
    while i+j+1<len(pat) and i-j>=0:
        if pat[i+j+1]!=pat[i-j]:
            return False
        j+=1
    # d=0
    # if i-j==0:d=i-j+1
    # else:d=i+j+1
    # print(d)
    # print(pat[d-1],pat[d])
    # if d==0:d+=1
    # for k in range(len(pat[0])):
    #     if pat[d][k]!=pat[d-1][k]:
    #         if pat[d][k]=='#':pat[d][k]='.'
    #         else: pat[d][k]='#'
    return True

def hor(pat):
    for i in range(len(pat)-1):
        if pat[i]==pat[i+1]:
            if check_hor(pat,i):
                return i+1
    return 0

def rot(pat):
    r=[]
    for e in pat[0]:r+=[[]]
    for j in range(len(pat)):
        for i in range(len(pat[0])):
            r[i]+=pat[j][i]
    return r

def value(pat):
    h=hor(pat)
    if h!=0:return h*100
    return hor(rot(pat))

# b=[list(e)for e in b]
# v=value(b)
# pat=b
# for i in range(len(pat)):
#     for j in range(len(pat[0])):
#         p=pat[i][j]
#         if p=='#':pat[i][j]='.'
#         else:pat[i][j]='#'
#         v2=value(pat)
#         if v2!=0 and v2!=v:break
#         pat[i][j]=p
# print(v2)

# f=[a,b]
t=u=0
for e in f:
    e=[list(v)for v in e]
    v=value(e)

    for i in range(len(e)):
        for j in range(len(e[0])):
            c=e[i][j]
            if c=='#':e[i][j]='.'
            else:e[i][j]='#'
            v2=value(e)
            if v2!=0 and v2!=v:break
            e[i][j]=c
    t+=v
    u+=v2

print(t,u)

# print("part 1:",t,"\npart 2:",u)
