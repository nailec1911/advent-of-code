from collections import defaultdict
from functools import cache

@cache
def splitstone(e):
    if e == 0:
        return [1]
    s = str(e)
    n = len(s)
    if n % 2 == 0:
        mid = n // 2
        divisor = 10 ** mid
        a, b = divmod(e, divisor)
        return [a, b]
    return [e * 2024]

f = [e[:-1] for e in list(open("input.txt"))][0]
f = [int(e) for e in f.split()]

prev_count = defaultdict(int)
cycle = 0
for e in f:
    prev_count[e] += 1

while cycle < 75:
    next_count = defaultdict(int)
    for stone, count in prev_count.items():
        spl = splitstone(stone)
        for e in spl:
            next_count[e] += count
    prev_count = next_count
    cycle += 1

print(sum(prev_count.values()))
