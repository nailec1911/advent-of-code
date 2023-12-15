#!/usr/bin/python3
f=open('input.txt').read()[:-1]


def hash(val):
    v=0
    for l in val:v=(v+ord(l))*17%256
    return v

def remove(boxes,label):
    box=boxes[hash(label)]
    for e in box:
        if e[0]==label:box.remove(e)

def add(boxes,label,foc):
    box=boxes[hash(label)]
    for e in box:
        if e[0]==label:
            e[1]=foc
            return
    box+=[label,foc],

f=f.split(',')
boxes={i:[] for i in range(256)}

t=0
for e in f:
    t+=hash(e)
    if e[-1]=='-':
        remove(boxes,e[:-1])
    else:
        box,val=e.split('=')
        add(boxes,box,int(val))

print(t)
print(sum((box+1)*(i+1)*l[i][1] for box,l in boxes.items()for i in range(len(l))))
