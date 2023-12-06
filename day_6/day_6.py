#!/usr/bin/python3
q=lambda t,d:((-t-(s:=(t**2-4*d)**0.5))/(-2)-1e-9)//1+(-((-t+s)/(-2)+1e-9)//1)+1
f=[list(map(int,e.split(':')[1].split()))for e in list(open("input.txt"))]
s=1
for e in zip(*f):s*=q(*e)
print("part 1:",s,"\npart 2:",q(*[int(''.join(map(str,e)))for e in f]))
