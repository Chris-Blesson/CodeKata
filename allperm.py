from itertools import permutations
s=input();
per=list(permutations(s))
if len(per)==2 and len(set(s))==1:
	print(*per[0],sep="")
	exit()
for i in per:
	print(*i,sep="")
