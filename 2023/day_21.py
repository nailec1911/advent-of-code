#!/usr/bin/python3


f=[list(e[:-1]) for e in list(open("input.txt"))]

# f=[
# '...........',
# '......##.#.',
# '.###.##..#.',
# '..#.#...#..',
# '....#.#....',
# '.##..S####.',
# '.##..#...#.',
# '.......##..',
# '.##.#.####.',
# '.##..##.##.',
# '...........',
# ]
# f=[list(e)for e in f]

save=[e[::]for e in f]
save2=[e[::]for e in f]
x=y=0
while not 'S' in f[x]:x+=1

y=f[x].index('S')
f[x][y]='O'

dir=((0,1),(0,-1),(1,0),(-1,0))

def take_step(f):
    r=[e[::]for e in f]
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j]=='O':
                r[i][j]='.'
                for oi,oj in dir:
                    x=i+oi;y=j+oj
                    if 0<=x<len(f) and 0<=y<len(f[0]) and f[x][y]!='#':
                        r[x][y]='O'
    return r

def count(f):
    t=0
    for i in range(len(f)):
        t+=f[i].count('O')
    return t


for i in range(64):
    f=take_step(f)
print("part 1:",count(f))

save[x][y]='O'
for i in range(len(f)):
    save=take_step(save)
res_square1=count(save)
res_square2=count(take_step(save))
#once the square is filled, it switches between two states

# get the number of O after n steps starting at x,y
def compute_from(f,x,y,steps):
    save=[e[::]for e in f]
    save[x][y]='O'
    for i in range(steps):
        save=take_step(save)
    return count(save)

# down, top, left and right points
s1=compute_from(save2,len(save)-1,len(save)//2,130)
s2=compute_from(save2,0,len(save)//2,130)
s3=compute_from(save2,len(save)//2,0,130)
s4=compute_from(save2,len(save)//2,len(save)-1,130)

# small sides
q1=compute_from(save2,0,0,64)
q2=compute_from(save2,0,len(save)-1,64)
q3=compute_from(save2,len(save)-1,0,64)
q4=compute_from(save2,len(save)-1,len(save)-1,64)

#big sides
qb1=compute_from(save2,0,0,65+130)
qb2=compute_from(save2,0,len(save)-1,65+130)
qb3=compute_from(save2,len(save)-1,0,65+130)
qb4=compute_from(save2,len(save)-1,len(save)-1,65+130)

side=26501365//len(f)

r1=side**2*res_square2
r2=(side-1)**2*res_square1

print('part 2:',r1+r2  +s1+s2+s3+s4  +side*(q1+q2+q3+q4)  +(side-1)*(qb1+qb2+qb3+qb4))
