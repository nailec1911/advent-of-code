
from collections import defaultdict
from itertools import combinations
import networkx as nx

f = [
    "kh-tc",
    "qp-kh",
    "de-cg",
    "ka-co",
    "yn-aq",
    "qp-ub",
    "cg-tb",
    "vc-aq",
    "tb-ka",
    "wh-tc",
    "yn-cg",
    "kh-ub",
    "ta-co",
    "de-co",
    "tc-td",
    "tb-wq",
    "wh-td",
    "ta-ka",
    "td-qp",
    "aq-cg",
    "wq-ub",
    "ub-vc",
    "de-ta",
    "wq-aq",
    "wq-vc",
    "wh-yn",
    "ka-de",
    "kh-ta",
    "co-tc",
    "wh-qp",
    "tb-vc",
    "td-yn",

]

f = [e[:-1] for e in list(open("input.txt"))]
links = defaultdict(set)
computers = set()

networks = []
for l in f:
    a, b = l.split('-')
    links[a].add(b)
    links[b].add(a)
    computers.add(a)
    computers.add(b)

score = 0
done = set()
for c in computers:
    if not c.startswith('t'):
        continue
    for a,b in combinations(links[c], 2):
        t = tuple(sorted([a, b, c]))
        if a in links[b] and t not in done:
            score += 1
            done.add(t)
print(score)



graph = nx.Graph()
for l in f:
    a,b = l.split('-')
    graph.add_edge(a,b)
clique=max(nx.find_cliques(graph), key=len)
part2=",".join(sorted(clique))


print(part2)
