from math import floor
from numba import jit

f = [int(e[:-1]) for e in list(open("input.txt"))]

def get_next(seed):
    val = seed * 64
    res = (seed ^ val) % 16777216

    val = floor(res / 32)
    res = (res ^ val) % 16777216

    val = res * 2048
    return (res ^ val) % 16777216


def get_secret200(seed):
    seq = [0, 0, 0, 0]
    old = 0
    dif = {}
    for i in range(2000):
        mod = seed % 10
        seq.append(mod - old)
        seq.pop(0)
        old = mod
        seqkey = tuple(seq)
        if i > 3 and seqkey not in dif:
            dif[seqkey] = mod
        seed = get_next(seed)
    return seed, dif


diffs = {}
score = 0
i = 0
for e in f:
    print(i := i + 1, len(f))
    s, dif = get_secret200(e)
    for key,val in dif.items():
        if key in diffs:
            diffs[key] += val
        else: diffs[key] = val
    score += s

print("part 1 :", score)
print("part 2 :", max(diffs.values()))
