#!/usr/bin/python3
f=list(open('input.txt'))

# "L|7||\n",
# "-L-J|\n",
# "L|-JF\n"]
# f=["..F7.\n",
#    ".FJ|.\n",
#    "SJ.L7\n",
#    "|F--J\n",
#    "LJ...\n"]

# f=[
# "...........\n",
# ".S-------7.\n",
# ".|F-----7|.\n",
# ".||.....||.\n",
# ".||.....||.\n",
# ".|L-7.F-J|.\n",
# ".|..|.|..|.\n",
# ".L--J.L--J.\n",
# "...........\n"]

# f=["FF7FSF7F7F7F7F7F---7\n",
# "L|LJ||||||||||||F--J\n",
# "FL-7LJLJ||||||LJL-77\n",
# "F--JF--7||LJLJ7F7FJ-\n",
# "L---JF-JLJ.||-FJLJJ7\n",
# "|F|F-JF---7F7-L7L|7|\n",
# "|FFJF7L7F-JF7|JL---7\n",
# "7-L-JL7||F7|L7F-7F7|\n",
# "L.L7LFJ|||||FJL7||LJ\n",
# "L7JLJL-JLJLJL--JLJ.L\n"]

f=[list(l[:-1])for l in f]

# that part is ugly don't look at it
conv={'|':('S7F|','SLJ|'), '-':('S-LF','S-7J'), 'L':('S|7F','S-J7'), 'J':('S-LF','S|7F'), '7':('S-LF','S|LJ'), 'F':('S|LJ','S-J7')}
next={'|':((-1,0),(1,0)), '-':((0,-1),(0,1)), 'L':((-1,0),(0,1)), 'J':((0,-1),(-1,0)), '7':((0,-1),(1,0)), 'F':((1,0),(0,1))}
p=[(-1,0),(1,0),(0,-1),(0,1)]

def next_step(c,k,z,pk,pz):
    a,b=next[c]
    if a==(pk,pz):a=b
    return k+a[0],z+a[1],-a[0],-a[1]

def start(f,i,j):
    for x,y in p:
        a,b=next[f[i-x][j-y]]
        if a==(x,y)or b==(x,y):
            return i-x,j-y,a[0],a[1]
    return i,j

# Find the start position
i=j=-1
while i<len(f) and j<0:
    i+=1
    if 'S' in f[i]:
        j=f[i].index('S')

save=[e[::] for e in f]

# go through all the path, replace with the distance
v=1
f[i][j]=0
i,j,pi,pj=start(f,i,j)
while f[i][j]!=0:
    c=f[i][j]
    f[i][j]=v
    i,j,pi,pj=next_step(c,i,j,pi,pj)
    v+=1

# find the char to replace S
for xp,yp in p:
    if f[i+xp][j+yp]==v-1:break
for xn,yn in p:
    if f[i+xn][j+yn]==1:break
for key,val in next.items():
    if ((xp,yp),(xn,yn))==val or ((xn,yn),(xp,yp))==val:S=key

# rebuild the path, remove all the one that aren't part of it
for k in range(len(f)):
    for l in range(len(f[0])):
        if type(f[k][l])!=int:
            save[k][l]='.'
        if f[k][l]==0:save[k][l]=S


f=save
i=j=0
while i<len(f):
    j=0
    d=0
    while j<len(f[0]):
        if f[i][j]=='|':d+=1
        #check if the turn is a U (not wall) or if it goes down (wall)
        if f[i][j] in 'L7FJ':
            c=f[i][j]
            j+=1
            while not f[i][j] in 'L7FJ': j+=1
            c+=f[i][j]
            if c=='L7' or c=='FJ':d+=1
        # if nb of wall before is odd, we are in the loop
        if d%2!=0 and f[i][j]=='.':f[i][j]='0'
        j+=1
    i+=1

# for e in f:
    # print(''.join(e))
t=0
for e in f:t+=e.count('0')
print("part 1:",v//2,"\npart 2:",t)
