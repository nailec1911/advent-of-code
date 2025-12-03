f = [e[:-1] for e in list(open("input.txt"))]

l = f[0].split(',')

# s = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
# l = s.split(",")

for i in range(len(l)):
    s, e = l[i].split('-')
    l[i] = [int(s), int(e)]

def invalid(id, rep):
    if len(id) % rep != 0:
        return False
    lenp = len(id) // rep

    for i in range(lenp):
        c = id[i]
        for j in range(rep):
            if id[lenp * j + i] != c:
                return False
    return True


res = 0
res2 = 0
for start, end in l:
    for i in range(start, end + 1):
        id = str(i)
        for j in range(2, len(id) + 1):
            if invalid(id, j):
                if j == 2:
                    res += i
                res2 += i
                break
9        # id = str(i)
        # leni = len(id)
        # for j in range(leni // 2, 0, -1):
            # pattern = id[:j]
            # lenp = len(pattern)
            # if leni % lenp != 0:
                # continue
#
            # d = leni // lenp
            # if pattern * d == id:
                # if d == 2:
                    # res += i
                # res2 += i
                # break

print(res)
print(res2)
