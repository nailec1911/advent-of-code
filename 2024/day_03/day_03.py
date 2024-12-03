f = open("input.txt").read()

# f = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# f = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def check(line: str) -> int:
    if line[:4] != "mul(":
        return 0
    end = 0
    i = 4
    while i < len(line):
        end += 1
        if line[i] == ')':
            break
        if not (line[i].isdigit() or line[i] == ','):
            break
        i += 1
    if line[i] != ')':
        return 0
    nbs = line[4:i]
    nb = nbs.split(',')
    if len(nb) != 2:
        return 0
    x, y = map(int, nb)
    return x * y


def do(line, old):
    if line[:4] == "do()":
        return True
    if line[:7] == "don't()":
        return False
    return old

score: int = 0
score2: int = 0
doe: bool = True
for a in range(len(f)):
    doe = do(f[a:], doe)
    t = check(f[a:])
    score += t
    if doe:
        score2 += t

print(score)
print(score2)
