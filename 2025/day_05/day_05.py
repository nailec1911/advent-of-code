f = [
"3-5",
"10-14",
"16-20",
"12-18",
"2-6",
"",
"1",
"5",
"8",
"11",
"17",
"32",
]
f = [e[:-1] for e in list(open("input.txt"))]



i = 0
ranges = []

while f[i] != '':
    a, b = f[i].split('-')
    ranges.append([int(a), int(b)])
    i += 1

merged = []
for a,b in sorted(ranges, key=lambda a: a[0]):
    if not merged or a > merged[-1][1]:
        merged.append([a, b])
    else :
        merged[-1][1] = max(merged[-1][1], b)

f = sorted([int(e) for e in f[i+1:]])

f.append(merged[-1][1] + 1) # just to be sure the lastrange is added for part 2
part1 = 0
res = 0
for elt in f:
    while merged and elt > merged[0][1]:
        a,b = merged.pop(0)
        res += b - a + 1
    if merged and merged[0][0] <= elt:
        part1 += 1


print(part1)
print(res)
