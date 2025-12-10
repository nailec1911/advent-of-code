from itertools import combinations, combinations_with_replacement


f = [
"[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
"[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
"[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]
f = [e[:-1] for e in list(open("input.txt"))]


def get_light(light):
    l = len(light) - 2
    binstr = light[-2:0:-1].translate(str.maketrans({'.': '0', '#': '1'}))
    return int(binstr, 2), l

def get_btn(btn):
    res = 0
    btn = [int(e) for e in btn[1:-1].split(',')]
    for e in btn:
        res |= 1 << (e)
    return res

def get_btn_vals(btn):
    return [int(e) for e in btn[1:-1].split(',')]

def results_btns(btns):
    nb = 0
    for x in btns:
        nb ^= x
    return nb


def get_res(to_push, lenght):
    l = [0 for _ in range(lenght)]
    for btns in to_push:
        for b in btns:
            l[b] += 1
    return l

def press_btn(btn, jolts):
    for b in btn:
        jolts[b] -= 1
    return jolts


grid = []
for i, line in enumerate(f):
    x = line.split(' ')
    lights, buttons, jolts = x[0], x[1:-1], x[-1]
    lights, len_lig = get_light(lights)
    btns2 = sorted([get_btn_vals(btn) for btn in buttons], key=lambda a: len(a), reverse=True)
    buttons = [get_btn(btn) for btn in buttons]
    jolts = get_btn_vals(jolts)
    grid.append([lights, buttons, btns2, jolts, len_lig])


part1 = 0
part2 = 0
i = 0
for light, buttons, btns2, jolts, len_lig in grid:
    # print(i)
    i += 1
    found = False
    length = 0
    while not found:
        length += 1
        possibilities = list(combinations(buttons, length))
        for pos in possibilities:
            res = results_btns(pos)
            if res == light:
                found = True
                part1 += length
                break

    # length = -1
    # while not -1 in jolts:
    #     length += 1
    #     jolts = press_btn(btns2[0], jolts)
    # for e in btns2[0]:
    #     jolts[e] += 1


    # found = False
    # l2 = 0
    # while not found:
    #     l2 += 1
    #     possibilities = list(combinations_with_replacement(btns2[1:], l2))
    #     for pos in possibilities:
    #         res = get_res(pos, len_lig)
    #         if res == jolts:
    #             found = True
    #             break
    #     if l2 > 13:
    #         for e in btns2[0]:
    #             jolts[e] += 1
    #         length -= 1
    #         l2 = 0
    #     print(length, l2)
    # part2 += length + l2

print(part1)
print(part2)
