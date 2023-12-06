#!/usr/bin/python3
def v(t,d,o):
 i=o*t
 while i*(t-i)<=d:i+=-o*2+1
 return i
w=lambda t:v(*t,1)-v(*t,0)+1
f=[[int(x)for x in e.split(':')[1].split(' ')if x]for e in open("input.txt","r").read().split('\n')]
s=1
for e in[z for z in zip(*f)]:s*=w(e)
print("part 1:",s,"\npart 2:",w([int(''.join(map(str,e)))for e in f]))
