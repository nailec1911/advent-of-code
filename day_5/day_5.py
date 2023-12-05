#!/usr/bin/python3

f = open("input.txt", "r").read().split('\n')

# f= ["seeds: 79 14 55 13",
#     "",
#     "seed-to-soil map:",
#     "50 98 2",
#     "52 50 48",
#     "",
#     "soil-to-fertilizer map:",
#     "0 15 37",
#     "37 52 2",
#     "39 0 15",
#     "",
#     "fertilizer-to-water map:",
#     "49 53 8",
#     "0 11 42",
#     "42 0 7",
#     "57 7 4",
#     "",
#     "water-to-light map:",
#     "88 18 7",
#     "18 25 70",
#     "",
#     "light-to-temperature map:",
#     "45 77 23",
#     "81 45 19",
#     "68 64 13",
#     "",
#     "temperature-to-humidity map:",
#     "0 69 1",
#     "1 0 69",
#     "",
#     "humidity-to-location map:",
#     "60 56 37",
#     "56 93 4"]

def get_list(f):
    f.pop(0)
    r=[]
    while f and f[0]!="":
        r.append([int(e) for e in f.pop(0).split(' ')])
    if f:f.pop(0)
    return r

def convert(seeds, conv):
    for i in range(len(seeds)):
        s=seeds.pop(0)
        v=0
        for c in conv:
            sta,end=max(s[0], c[1]),min(s[1], c[1]+c[2])
            if sta<end:
                v=1
                if s[0]<sta:seeds+=[s[0],sta],
                seeds+=[sta-c[1]+c[0],end-c[1]+c[0]],
                if end<s[1]:seeds+=[end,s[1]],
                break
        if v<1:seeds+=s,

seeds = [int(e) for e in f.pop(0)[7:].split(' ')]
pairs= [[seeds[i],seeds[i]+seeds[i+1]] for i in range(0,len(seeds),2)]
seeds=[[seeds[i],seeds[i]+1] for i in range(len(seeds))]
f.pop(0)

while f:
    conv=get_list(f)
    convert(seeds, conv)
    convert(pairs,conv)

print("part 1:",min(seeds)[0])
print("part 2:",min([e[0] for e in pairs]))
