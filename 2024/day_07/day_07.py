
from itertools import product


f = [
"190: 10 19",
"3267: 81 40 27",
"83: 17 5",
"156: 15 6",
"7290: 6 8 6 15",
"161011: 16 10 13",
"192: 17 8 14",
"21037: 9 7 18 13",
"292: 11 6 16 20",
]
# f = [e[:-1] for e in list(open("input.txt"))]

res = []

for e in f:
    a, b = e.split(':')

    tot = int(a)
    vals = b.split()
    vals = [int(d) for d in vals]
    res.append([tot, vals])


def ternary(n):
    e = n//3
    q = n%3
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e) + str(q)


def check(tot, vals, p2):
    combinations = [''.join(p) for p in product("+*|", repeat=len(vals) - 1)]
    for c in combinations:
        test = vals[0]
        for j in range(1, len(vals)):
            if c[j - 1] == '+':
                test *= vals[j]
            elif p2 and c[j - 1] == '|':
                test = int(str(test) + str(vals[j]))
            else:
                test += vals[j]
        if test == tot:
            return True
    return False



# def check(tot, vals, p2):
    # for i in range(3  ** (len(vals) - 1) + 1):
        # l = "0000000000000" + ternary(i)
        # test = vals[0]
        # for j in range(1, len(vals)):
            # if l[-j] == '0':
                # test *= vals[j]
            # elif p2 and l[-j] == '1':
                # test = test and vals[j]
            # else:
                # test += vals[j]
        # if test == tot:
            # return True
    # return False



score = 0
score2 = 0
i = 0
for elt in res:
    i += 1
    print(i, len(res))
    if check(*elt, False):
        score += elt[0]
    if check(*elt, True):
        score2 += elt[0]

print(score, score2)
