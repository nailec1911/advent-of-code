#!/usr/bin/python3
def s(l,a,j,t):
 for i,b in enumerate('one,two,three,four,five,six,seven,eight,nine'.split(',')):
  if t and l[j:][:len(b)]==b:return-~i
 return int(l[j].isdigit()and l[j]or s(l,a,j+a,t))
def r(a,t=0):
 for l in open("input","r").readlines():t+= s(l,1,0,a)*10+s(l,-1,-1,a)
 return t
print("part 1:",r(0),"part 2:",r(1))
