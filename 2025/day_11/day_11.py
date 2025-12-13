f = [
["aaa", "you hhh"],
["you", "bbb ccc"],
["bbb", "ddd eee"],
["ccc", "ddd eee fff"],
["ddd", "ggg"],
["eee", "out"],
["fff", "out"],
["ggg", "out"],
["hhh", "ccc fff iii"],
["iii", "out"],
]

f = [
["svr", "aaa bbb"],
["aaa", "fft"],
["fft", "ccc"],
["bbb", "tty"],
["tty", "ccc"],
["ccc", "ddd eee"],
["ddd", "hub"],
["hub", "fff"],
["eee", "dac"],
["dac", "fff"],
["fff", "ggg hhh"],
["ggg", "out"],
["hhh", "out"],
]


from functools import cache
f = [e[:-1].split(": ") for e in list(open("input.txt"))]

graph = {}
for node, conn in f:
    outs = conn.split(' ')
    graph[node] = outs

def dept_search(graph, node):
    if node == "out":
        return 1
    outs = graph[node]
    print(outs)
    if not outs:
        return 0
    return sum(dept_search(graph, out) for out in outs)

@cache
def dept_search2(node, fft, dac):
    if node == "out":
        return 1 if fft and dac else 0
    outs = graph[node]
    if "fft" == node:
        fft = True
    if "dac" == node:
        dac = True
    if not outs:
        return 0
    return sum(dept_search2(out, fft, dac) for out in outs)

# print(dept_search(graph, "you"))
print(dept_search2("svr", False, False))
