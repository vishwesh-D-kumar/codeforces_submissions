n=int(input())
x=list(map(int,input().split()))
e=0
o=0
for i in x:
	if i%2==0:
		e+=1
	else:
		o+=1
	if e and o:
		break
if e==n or o==n:
	for i in x:
		print(i,end=" ")
else:
	x.sort()
	for i in x:
		print(i,end=" ")