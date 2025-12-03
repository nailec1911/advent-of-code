f = [[int(b) for b in e[:-1]] for e in list(open("input.txt"))]

# f= [
# "987654321111111",
# "811111111111119",
# "234234234234278",
# "818181911112111",
# ]
# f = [[int(e) for e in b] for b in f]

# This is not the first solution I had, my first was
# a more classic and bit longer iterative thing


def get_val(line, stage):
    if stage < 0:
        return 0
    idx = line.index(max(line[:len(line) - stage]))
    return get_val(line[idx + 1:], stage - 1) + line[idx] * 10 ** stage


print(sum(get_val(b, 1) for b in f))
print(sum(get_val(b, 11) for b in f))
