f = [e[:-1] for e in list(open("input.txt"))]

keys = []
locks = []
elts = [locks, keys]
is_key = '.' in f[0]
elts[is_key].append([])
for i, line in enumerate(f):
    if line == "":
        is_key = '.' in f[i + 1]
        elts[is_key].append([])
        continue
    elts[is_key][-1].append(line)


def to_vals(blocks, is_key):
    res = []
    for key in blocks:
        res.append([])
        for i in range(len(key[0])):
            j = 0
            while j < len(key) and key[-(j + 1) if is_key else j][i] == '#':
                j += 1
            res[-1].append(j - 1)
    return res


def keys_compatible(lock, key):
    return all(map(lambda a: sum(a) <= 5, zip(lock, key)))


keys_val = to_vals(keys, True)
locks_val = to_vals(locks, False)
score = 0
for i, key in enumerate(keys_val):
    for j, lock in enumerate(locks_val):
        if keys_compatible(lock, key):
            score += 1

print(score)
