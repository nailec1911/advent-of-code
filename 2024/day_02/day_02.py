
def check(line : list[int]) -> bool:
    inc: bool = True
    if line[0] > line[1]:
        inc = False

    for i in range(len(line) - 1):
        diff: int = line[i + 1] - line[i]
        if not inc:
            diff = -diff
        if (diff < 1 or diff > 3):
            return False
    return True


def check2(lvl: list[int]) -> bool:
    if check(lvl):
        return True
    for i in range(len(lvl)):
        new = lvl[:i ] + lvl[i + 1:]
        if check(new):
            return True
    return False



f = [e[:-1] for e in list(open("input.txt"))]
# f = [
# "7 6 4 2 1",
# "1 2 7 8 9",
# "9 7 6 2 1",
# "1 3 2 4 5",
# "8 6 4 4 1",
# "1 3 6 7 9"]

nbs: list[list[int]] = []
for e in f:
    nbs.append(list(map(int, e.split())))

nbsafe: int = 0
nbsafe2: int = 0

for level in nbs:
    if check(level):
        nbsafe += 1
    if check2(level):
        nbsafe2 += 1

print("part 1 :", nbsafe)
print("part 2 :", nbsafe2)
