def get_val_combo(v, ra, rb, rc):
    if 0 <= v <= 3:
        return v
    if v == 4:
        return ra
    if v == 5:
        return rb
    if v == 6:
        return rc
    return 7


def run_prog(prog, ra, rb, rc):
    out = []
    i = 0
    while i < len(prog):

        opcode = prog[i]
        if opcode == 0:
            denom = get_val_combo(prog[i + 1], ra, rb, rc)
            ra = ra // (2 ** denom)
            i += 2

        if opcode == 1:
            rb ^= prog[i + 1]
            i += 2

        if opcode == 2:
            # rb = get_val_combo(prog[i + 1], ra, rb, rc) & 8
            rb = get_val_combo(prog[i + 1], ra, rb, rc) % 8
            i += 2

        if opcode == 3:
            if ra != 0:
                i = prog[i + 1]
                continue
            i += 2

        if opcode == 4:
            rb = rb ^ rc
            i += 2

        if opcode == 5:
            out.append(get_val_combo(prog[i + 1], ra, rb, rc) % 8)
            i += 2

        if opcode == 6:
            denom = get_val_combo(prog[i + 1], ra, rb, rc)
            rb = ra // (2 ** denom)
            i += 2

        if opcode == 7:
            denom = get_val_combo(prog[i + 1], ra, rb, rc)
            rc = ra // (2 ** denom)
            i += 2
    return out

def test(ra):
    rb = 0
    rc = 0

    rb = ra % 8
    rb = rb ^ 2
    rc = ra // (2 ** rb)
    rb = rb ^ rc
    rb = rb ^ 3
    # out ==== rb % 8
    ra = ra // (2 ** 3)
    return rb % 8, ra


def add_layer(searched, old):
    new = set()
    for e in old:
        for i in range(8):
            num = (e << 3) + i
            if test(num)[0] == searched:
                new.add(num)
    return new



reg_a = 27575648
reg_b = 0
reg_c = 0

program = [2, 4, 1, 2, 7, 5, 4, 1, 1, 3, 5, 5, 0, 3, 3, 0]

output = run_prog(program, reg_a, reg_b, reg_c)
print(','.join(str(o) for o  in output))

res = {0}
for x in reversed(program):
    res = add_layer(x, res)
print(min(res))
