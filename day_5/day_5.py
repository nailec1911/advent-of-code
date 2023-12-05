#!/usr/bin/python3

f = open("input.txt", "r").read().split('\n')

# f= ["seeds: 79 14 55 13",
    # "",
    # "seed-to-soil map:",
    # "50 98 2",
    # "52 50 48",
    # "",
    # "soil-to-fertilizer map:",
    # "0 15 37",
    # "37 52 2",
    # "39 0 15",
    # "",
    # "fertilizer-to-water map:",
    # "49 53 8",
    # "0 11 42",
    # "42 0 7",
    # "57 7 4",
    # "",
    # "water-to-light map:",
    # "88 18 7",
    # "18 25 70",
    # "",
    # "light-to-temperature map:",
    # "45 77 23",
    # "81 45 19",
    # "68 64 13",
    # "",
    # "temperature-to-humidity map:",
    # "0 69 1",
    # "1 0 69",
    # "",
    # "humidity-to-location map:",
    # "60 56 37",
    # "56 93 4"]
#
def get_list(f):
    f.pop(0)
    r=[]
    while f and f[0]!="":
        r.append([int(e) for e in f.pop(0).split(' ')])
    if f:f.pop(0)
    return r

def in_r(conv, seed): return seed in range(conv[1],conv[1]+conv[2])
def convert(seeds, conv):
    r=[]
    for s in seeds:
        v=0
        for c in conv:
            if in_r(c, s): r+=c[0]+s-c[1],;v=1
        if v<1: r+=s,

    return r

seeds = [int(e) for e in f.pop(0)[7:].split(' ')]
pairs= [[seeds[i],seeds[i+1]] for i in range(0,len(seeds),2)]
f.pop(0)

# s2=[e for v in pairs for e in range(v[0],v[0]+v[1])]
while f:
    conv=get_list(f)
    seeds=convert(seeds, conv)
    # s2=convert(s2,conv)

print("part 1:",min(seeds))
# print("part 2:",min(s2))
