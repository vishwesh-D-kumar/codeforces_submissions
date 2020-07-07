n=int(input())
x=[]
s1=0
s2=0
x=list(map(int,input().split()))
same=x[0]==x[1]
for i in range(2*n):
	if same:
		same=x[0]==x[i]
	if i<n:
		s1+=x[i]
	else:
		s2+=x[i]
if s1!=s2:
	for i in x:
		print(i,end=" ")
else:
	if same:
		print(-1)
	else:
		for i in range(n):
			if x[i]!=x[-1]:
				x[i],x[-1]=x[-1],x[i]
				break;

		for i in x:
			print(i,end=" ")

