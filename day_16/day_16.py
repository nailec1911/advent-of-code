#!/usr/bin/python3
f=[e[:-1] for e in list(open("input.txt"))]

# f=[
# '.|...\....',
# '|.-.\.....',
# '.....|-...',
# '........|.',
# '..........',
# '.........\\',
# '..../.\\\\..',
# '.-.-/..|..',
# '.|....-|.\\',
# '..//.|....',
# ]

def energize(f,start):
    beams=[start]
    t=set()
    done=set()
    while beams:
        i,j,x,y=beams.pop()
        if (i,j,x,y)in done:continue
        if not(0<=i<lf and 0<=j<lf0):continue
        done.add((i,j,x,y))
        t.add((i,j))
        if f[i][j]=='.':
            done.add((i,j,x,y))
            while (0<=i<lf and 0<=j<lf0) and (f[i][j]=='.'):
                t.add((i,j))
                i+=x;j+=y
            beams.append((i,j,x,y))
            continue
        match f[i][j],x:
            case ['\\',_]:
                x,y=y,x
                beams.append((i+x,j+y,x,y))
            case ['/',_]:
                x,y=-y,-x
                beams.append((i+x,j+y,x,y))
            case ['-',-1|1]:
                if x:
                    beams.append((i,j-1,0,-1))
                    beams.append((i,j+1,0,1))
            case ['|',0]:
                if y:
                    beams.append((i-1,j,-1,0))
                    beams.append((i+1,j,1,0))
            case _: beams.append((i+x,j+y,x,y))
    return len(t)


t=[]
lf,lf0=len(f),len(f[0])
for i in range(lf):
    # print(i)
    t+=energize(f,(i,0,0,1)),
    t+=energize(f,(i,lf0-1,0,-1)),
# print('####################################')
for j in range(lf0):
    # print(j)
    t+=energize(f,(0,j,1,0)),
    t+=energize(f,(lf-1,j,-1,0)),
# for e in f:print(''.join(e))
# print(t)
print("part 1:",t[0],"\npart 2:",max(t))
