a = ["3   4\n",
"4   3\n",
"2   5\n",
"1   3\n",
"3   9\n",
"3   3\n" ]



f=[e[:-1] for e in list(open("input.txt"))]
# f=[e[:-1] for e in list(a)]


f = [e.split() for e in f]


right = []
left = []

for e in f:
    left.append(int(e[0]))
    right.append(int(e[1]))



tot = 0

right.sort()
left.sort()

sim = {}

for i in range(len(right)):
    if right[i] in sim.keys():
        sim[right[i]] += 1
    else:
        sim[right[i]] = 1
    a = abs(right[i] - left[i])
    tot += a

print("part1", tot)

tot = 0
for e in left:
    if e in sim.keys():
        tot += e * sim[e]

print(tot)
