#!/usr/bin/python3

f=[list(l[:-1])for l in list(open('input.txt'))]

ne={'|':'ud','-':'lr','L':'ur','J':'lu','7':'ld','F':'dr'}
co={'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
p=co.values()

i=j=-1
while(i<len(f))-('S'in f[i]):i+=1
j=f[i].index('S')

s=[e[::] for e in f]

f[i][j]=0
for x,y in p:
    a,b=ne[f[i-x][j-y]]
    if co[a]==(x,y)or co[b]==(x,y):break
i-=x
j-=y
v=1
while f[i][j]!=0:
    c,f[i][j]=f[i][j],v
    a,b=ne[c]
    a,b=co[a],co[b]
    if type(f[i+a[0]][j+a[1]])==int:a=b
    i+=a[0];j+=a[1]
    v+=1

# find the char to replace S
for xp,yp in p:
    if f[i+xp][j+yp]==v-1:break
for xn,yn in p:
    if f[i+xn][j+yn]==1:break
for key,val in ne.items():
    if ((xp,yp),(xn,yn))==(co[val[0]],co[val[1]])or((xn,yn),(xp,yp))==val:S=key

# rebuild the path, remove all the one that aren't part of it
for k in range(len(f)):
 for l in range(len(f[0])):
  if type(f[k][l])!=int:s[k][l]='.'
  if f[k][l]==0:s[k][l]=S

f=s
i=j=0
while i<len(f):
    j=d=0
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
