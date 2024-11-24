#!/usr/bin/python3
# OFF : 0     ON : 1
# LOW : 0     HIGH : 1

nodes={'rx':['rx',[],{},0]}
for n in list(open("input.txt")):
    name,_,*dest=n.replace(',','').split()
    t,name=name[0],name[1:]
    nodes[name]=[t,dest,{},0]

to_search=''
for key,item in nodes.items():
    for dest in item[1]:
        nodes[dest][2][key]=0

prevs={k:0 for k,item in nodes.items() for dest in item[1] if 'rx' in nodes[dest][1]}

# pulse : dest, value, sender
t=[0,0]
count=0
while 0 in prevs.values():
    count+=1
    pulses=[['roadcaster',0,'button']]
    while pulses:
        current,val,sender=pulses.pop(0)
        type,dest,conj,flip=nodes[current]

        if count<1001:t[val]+=1

        if 'rx'in dest:
            if val:prevs[sender]=count

        match type:
            case '%':
                if val:continue
                nodes[current][3]=val=flip^1
            case '&':
                conj[sender]=val
                val=not all(conj.values())
            case 'rx':continue
        pulses+=[[d,val,current]for d in dest]

lcm=1
for nb in prevs.values():
    a,b=lcm,nb
    while b!=0:a,b=b,a%b
    lcm=lcm*nb//a

print("part 1:",t[0]*t[1],"\npart 2:",lcm)
