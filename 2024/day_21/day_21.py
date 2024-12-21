from functools import cache
f = [e[:-1] for e in list(open("input.txt"))]

# f = [
    # "029A",
    # "980A",
    # "179A",
    # "456A",
    # "379A",
# ]
# tot = ['<A^A>^^AvvvA', '^^^A<AvvvA>A',
    #    '^<<A^^A>>AvvvA', '^^<<A>A>AvvA', '^A<<^^A>>AvvvA']

# 789
# 456
# 123
#  0A

# I need to find a way to do this automatically
tot = [['<^^A<A>vvA>A', '^<^A<A>vvA>A', '^^<A<A>vvA>A', '<^^A<Av>vA>A', '^<^A<Av>vA>A', '^^<A<Av>vA>A'],
       ['<^^A^AvvAv>A', '^<^A^AvvAv>A', '^^<A^AvvAv>A', '<^^A^AvvA>vA', '^<^A^AvvA>vA', '^^<A^AvvA>vA'],
       ['^<<A^>>A^AvvvA', '<^<A^>>A^AvvvA', '^<<A>^>A^AvvvA', '<^<A>^>A^AvvvA', '^<<A>>^A^AvvvA', '<^<A>>^A^AvvvA'],
       ['<^^A^>AvvAvA', '^<^A^>AvvAvA', '^^<A^>AvvAvA', '<^^A>^AvvAvA', '^<^A>^AvvAvA', '^^<A>^AvvAvA'],
       ['<^^A<^A>>AvvvA', '^<^A<^A>>AvvvA', '^^<A<^A>>AvvvA', '<^^A^<A>>AvvvA', '^<^A^<A>>AvvvA', '^^<A^<A>>AvvvA']
]


@cache
def get_cheapest_move(move, depth):
    move2 = {'AA': [''], 'A^': ['<'], 'A>': ['v'], 'Av': ['<v', 'v<'], 'A<': ['v<<', '<v<'],
             '^^': [''], '^A': ['>'], '^>': ['v>', '>v'], '^v': ['v'], '^<': ['v<'],
             '<<': [''], '<^': ['>^'], '<>': ['>>'], '<v': ['>'], '<A': ['>>^', '>^>'],
             'vv': [''], 'v^': ['^'], 'v>': ['>'], 'vA': ['>^', '^>'], 'v<': ['<'],
             '>>': [''], '>^': ['<^', '^<'], '>A': ['^'], '>v': ['<'], '><': ['<<']}
    sols = [get_cheapest_sol(m + 'A', depth - 1) for m in move2[move]]
    return min(sols)


def get_cheapest_sol(line, depth):
    if depth <= 1:
        return len(line)
    todo = 'A'
    res = 0
    for c in line:
        todo += c
        res += get_cheapest_move(todo, depth)
        todo = todo[1:]
    return res

codes = [int(e[:-1]) for e in f]
score = 0
score2 = 0
for i, lines in enumerate(tot):
    res1 = min([get_cheapest_sol(line, 3) for line in lines])
    res2 = min([get_cheapest_sol(line, 26) for line in lines])
    score += res1 * codes[i]
    score2 += res2 * codes[i]
print(score)
print(score2)
