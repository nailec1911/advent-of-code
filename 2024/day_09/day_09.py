f = [e[:-1] for e in list(open("input.txt"))]
f = f[0]

# f = "2333133121414131402"
# f = "12345"

disk = []
id = 0
for i in range(0, len(f), 2):
    size = int(f[i])
    free = 0
    if i < len(f) - 1:
        free = int(f[i + 1])
    for j in range(size):
        disk.append(id)
    for j in range(free):
        disk.append('.')
    id += 1


# move at the begining by block (part 1)
# j = len(disk) - 1
# for i in range(len(disk)):
#     if disk[i] != '.': continue
#     while j > 0 and disk[j] == '.':
#         j -= 1
#     if j <= i: break
#     disk[i], disk[j] = disk[j], disk[i]


# move at the begining by file (part 2)
j = len(disk) - 1
i = 0
while j > 0 :
    while j > 0 and disk[j] == '.':
        j -= 1
    size = 0
    while disk[j - size] == disk[j]: size += 1
    free = 0
    i = 0
    while free < size:
        i += 1
        if disk[i] != '.': continue
        if i > j: break
        free = 0
        while i + free < len(disk) and disk[i + free] == '.':
            free += 1
    print(j)
    if i > j:
        j -= size
        continue

    for m in range(size):
        disk[i], disk[j - m] = disk[j - m], disk[i]
        i +=1
    j -= 1

# compute checksum
score = 0
for i in range(len(disk)):
    if disk[i] == '.': continue
    score += disk[i] * i

print(score)
