row,col=input().split()
col=int(col)
values=input().rstrip()
values=list(map(str,values.split(" ")))
for i in range(col):
	nodes=input()
	nodes=list(map(int,nodes.split(" ")))
	temp=values[nodes[0]-1:nodes[1]]
	print(min(temp))