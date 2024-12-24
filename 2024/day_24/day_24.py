from itertools import combinations

f = [e[:-1] for e in list(open("input.txt", encoding='utf-8'))]
separator = f.index('')

start = {}
for line in f[:separator]:
    wire, val_bin = line.split(' ')
    val_bin = int(val_bin)
    start[wire[:-1]] = val_bin

SIZE = len(start) // 2

operations = []
for line in f[separator + 1:]:
    wire1, op, wire2, _, wire3 = line.split(' ')
    operations.append([wire1, op, wire2, wire3, False])

ops = {"AND": lambda a, b: a & b, "OR": lambda a,
       b: a | b, "XOR": lambda a, b: a ^ b}

while any([not a[-1] for a in operations]):
    for i, op in enumerate(operations):
        wire1, op, wire2, wire3, _ = op
        if not (wire1 in start and wire2 in start):
            continue
        res = ops[op](start[wire1], start[wire2])
        start[wire3] = res
        operations[i][-1] = True

l = sorted([elt for elt in start.items() if elt[0][0] == 'z'])
l = [str(e[1]) for e in l[::-1]]
print(int(''.join(l), 2))


def check_op(links, w1, keyword, w2):
    for e in links:
        if (e[0] == w1 and e[2] == w2 and e[1] == keyword) or (e[0] == w2 and e[2] == w1 and e[1] == keyword):
            return e[3]
    return None


def find_index_error(idx, ok):
    for i in range(idx, SIZE):
        x = f"x{i:02}"
        y = f"y{i:02}"

        val = check_op(operations, x, "XOR", y)
        temp_carry = check_op(operations, x, "AND", y)
        if i == 0:
            carries[0] = temp_carry
            continue
        carry = carries[i - 1]

        temp = check_op(operations, carry, "AND", val)
        resz = check_op(operations, carry, "XOR", val)
        if resz != f"z{i:02}":
            return i, ok, [temp_carry, val, temp, resz, carry]

        ok.add(temp_carry)
        ok.add(val)
        ok.add(temp)
        ok.add(resz)
        carries[i] = check_op(operations, temp, "OR", temp_carry)
        ok.add(carry)

    return 44, ok, [temp_carry, val, temp, resz, carry]


carries = {}
swaps = []
used = set()
to_change, used, wrongs = find_index_error(0, used)

for _ in range(4):
    for i, j in combinations(range(len(operations)), 2):
        res_i = operations[i][3]
        res_j = operations[j][3]

        if not (res_i in wrongs or res_j in wrongs):
            continue
        if res_i in used or res_j in used:
            continue
        operations[i][3] = res_j
        operations[j][3] = res_i
        new, new_used, new_wrongs = find_index_error(to_change, used)
        if new > to_change:
            swaps += [res_i, res_j]
            to_change, used, wrongs = new, new_used, new_wrongs
            break
        operations[i][3] = res_i
        operations[j][3] = res_j

print(','.join(sorted(swaps)))
