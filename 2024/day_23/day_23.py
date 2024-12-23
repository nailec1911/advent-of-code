import networkx as nx

f = [e[:-1] for e in list(open("input.txt"))]

graph = nx.Graph()
for l in f:
    a, b = l.split('-')
    graph.add_edge(a, b)


def check_clique(c):
    return len(c) == 3 and any([e.startswith('t') for e in c])


print(sum(map(check_clique, nx.enumerate_all_cliques(graph))))

clique = max(nx.find_cliques(graph), key=len)

print(",".join(sorted(clique)))
