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
# f=[list(e)for e in f]

d={'\\':1,'/':-1}

def energize(f,start):
    beams=[start]
    t=[]
    done=[]
    while beams!=[]:
        i,j,x,y=beams.pop(0)
        if [i,j,x,y]in done:continue
        done.append([i,j,x,y])
        if not (0<=i<len(f) and 0<=j<len(f[0])):
            continue
        c=f[i][j]
        # if c=='.':
        #     f[i][j]='v' if x==1 else '^'if x==-1 else '>'if y==1 else '<'
        if not (i,j) in t:t+=(i,j),
        if c in '\\/':
            x,y=d[c]*y,d[c]*x
            beams.append([i+x,j+y,x,y])
            continue
        if c=='-' and x!=0:
            beams.append([i,j-1,0,-1])
            beams.append([i,j+1,0,1])
            continue
        if c=='|' and y!=0:
            beams.append([i-1,j,-1,0])
            beams.append([i+1,j,1,0])
            continue
        beams.append([i+x,j+y,x,y])
    return len(t)

t=[]
for i in range(len(f)):
    print(i)
    t+=energize(f,[i,0,0,1]),
    t+=energize(f,[i,len(f[0])-1,0,-1]),
print('####################################')
for j in range(len(f[0])):
    print(j)
    t+=energize(f,[0,j,1,0]),
    t+=energize(f,[len(f)-1,j,-1,0]),
# for e in f:print(''.join(e))
# print(t)
print(t[0],max(t))
