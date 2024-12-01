from collections import Counter

# example = ["3   4\n",
# "4   3\n",
# "2   5\n",
# "1   3\n",
# "3   9\n",
# "3   3\n" ]
# f=[e[:-1] for e in list(example)]

f = [e[:-1] for e in list(open("input.txt"))]


right = []
left = []
for e in f:
    l, r = e.split()
    left.append(int(l))
    right.append(int(r))

right.sort()
left.sort()
sim = Counter(right)

print(sum(abs(a - b)for a, b in zip(left, right)))
print(sum(e * sim[e] for e in left))
