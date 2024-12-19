from functools import cache

f = [e[:-1] for e in list(open("input.txt"))]
possible_patterns = f[0].split(', ')
f = f[2:]


@cache
def get_possibilities(design) -> int:
    if design == "":
        return 1
    possible = 0
    for e in possible_patterns:
        if design[:len(e)] == e:
            possible += get_possibilities(design[len(e):])
    return possible


score = 0
score2 = 0
i = 0
for towel in f:
    print(i := i + 1, len(f))

    t = get_possibilities(towel)
    score += t > 0
    score2 += t

print(score)
print(score2)
