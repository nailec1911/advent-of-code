f = [e[:-1] for e in list(open("input.txt"))]
separator = f.index('')

start = {}
for line in f[:separator]:
    wire, val = line.split(' ')
    val = int(val)
    start[wire[:-1]] = val

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

l = []
for key, val in start.items():
    if not key.startswith('z'):
        continue
    l.append((key, val))
l.sort()

score: int = 0
for z, val in reversed(l):
    score <<= 1
    score |= val

print(score)


def search(links, w1, keyword, w2, w3):
    for i, e in enumerate(links):
        if (e[0] == w1 and e[1] == keyword and e[2] == w2) or (e[0] == w2 and e[1] == keyword and e[2] == w1):
            if e[3] == w3:
                return True, i
            return False, i
    return False, -1


def check_op(links, w1, keyword, w2, w3=""):
    for i, e in enumerate(links):
        if (e[0] == w1 and e[1] == keyword and e[2] == w2) or (e[0] == w2 and e[1] == keyword and e[2] == w1):
            if w3 == "":
                return True, i
            if e[3] == w3:
                return True, i
            return False, i
    return False, -1


def find_res(links, w3):
    for i, e in enumerate(links):
        if e[3] == w3:
            return i
    return 0


check_op(operations, "x00", "XOR", "y00", "z00")
ok, idx = check_op(operations, "x00", "AND", "y00")
carry = operations[idx][3]
before = idx
not_ok = set()

for i in range(1, SIZE):
    x = f"x{i:02}"
    y = f"y{i:02}"
    z = f"z{i:02}"
    print(x, y, z)

    # carry : rfd
    ok, idx = check_op(operations, x, "XOR", y)
    val = operations[idx][3]  # smf
    if not ok:
        not_ok.add(i)

    ok, idx = check_op(operations, x, "AND", y)
    temp_carry = operations[idx][3]  # wkw
    if not ok:
        not_ok.add(i)

    ok, idx = check_op(operations, carry, "AND", val)
    temp = operations[idx][3]  # jgr
    if not ok:
        not_ok.add(i)

    ok, idx = check_op(operations, carry, "XOR", val, z)  # fcd
    if not ok:
        not_ok.add(i)

    ok, idx = check_op(operations, temp, "OR", temp_carry)
    carry = operations[idx][3]
    before = idx
    if not ok:
        not_ok.add(i)
    if i in not_ok:
        print("ooooooooooooo")


# z16,hmk
# z20,fhp
# tpc,rvf
# z33,fcd
