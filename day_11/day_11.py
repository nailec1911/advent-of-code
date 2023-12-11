#!/usr/bin/python3
f=list(open('input.txt'))

f=[
"...#......\n",
".......#..\n",
"#.........\n",
"..........\n",
"......#...\n",
".#........\n",
".........#\n",
"..........\n",
".......#..\n",
"#...#.....\n"]
f=[list(e[:-1])for e in f]

def empty_line(f,i): return not '#' in f[i]
def empty_col(f,j): return not '#' in [l[j]for l in f]

# # i=0
# # while i<len(f):
#     # if empty_line(f,i):
#         # for j in range(9):
#             # f.insert(i, f[i][::])
#         # i+=10
#     # i+=1
# # i=0
# # while i<len(f[0]):
#     # if empty_col(f,i):
#         # for z in range(9):
#             # for j in range(len(f)):
#                 # f[j].insert(i,'.')

#         # i+=10
#     # i+=1
# #
# # for e in f:
# #     print(''.join(e))
# # def dist(i,j,k,l):
#     # print(i,j,k,l)
#     # return  k-i+abs(l-j)

# # def check_all(f,i,j):
#     # r=0
#     # for k in range(i,len(f)):
#         # for l in range(len(f[0])):
#             # if f[k][l]=='#':
#                 # r+=dist(i,j,k,l)
#     # return r
# # t=0
# # for i in range(len(f)):
#     # for j in range(len(f[0])):
#         # if f[i][j]=='#':
#             # f[i][j]='.'
#             # t+=check_all(f,i,j)
# # print(t)
# # exit()

large=[e[::]for e in f]
large.append([i for i in range(len(f[0]))])
for i in range(len(large)):
    large[i].insert(0,i)

f=[e[::]for e in large]


i=0
while i<len(f):
    if empty_line(f,i):
        for j in range(i,len(f)):
            f[j][0]+=1
            large[j][0]+=99
        i+=1
    i+=1
i=1
while i<len(f[0]):
    if empty_col(f,i):
        for j in range(i,len(f[0])):
            f[-1][j]+=1
            large[-1][j]+=99

    i+=1


def dist(i,j,k,l):
    print(i,j,k,l)
    return  k-i+abs(l-j)

def check_all(f,i,j):
    r=0
    for k in range(i,len(f)):
        for l in range(len(f[0])):
            if f[k][l]=='#':
                r+=dist(f[i][0],f[-1][j],f[k][0],f[-1][l])
    return r

t=0
t2=0
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j]=='#':
            f[i][j]='.'
            large[i][j]='.'
            # t+=check_all(f,i,j)
            t2+=check_all(large,i,j)
print(t,t2)
