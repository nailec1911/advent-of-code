from functools import cmp_to_key

# I am really proud of my solution for this day

f = [e[:-1] for e in list(open("input.txt"))]
separator = f.index('')

# creating the dictionnary corresponding to the first part (number orders)
ordering = {i:[] for i in range(100)}
for e in f[:separator]:
    x, y = map(int, e.split('|'))
    ordering[x].append(y)


# for each set of updates, we sort it and then get the middle
scores = [0, 0]
for e in f[separator + 1:]:
    # parse the line
    updates = [int(nb) for nb in e.split(',')]

    # sort the list, the lamba search throught the order to check if we need to swap elts or not ( * 2 - 1 is used to convert bool to 1 or -1)
    new = sorted(updates, key=cmp_to_key(lambda a, b: (a in ordering[b]) * 2 - 1))

    # if it was sorted, we add middle to part1, else it's on part 2
    scores[updates != new] += new[len(new) // 2]

print(*scores)
