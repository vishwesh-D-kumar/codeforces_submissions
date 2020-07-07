n=int(input())
x=list(map(int,input().split()))

def o(n):
	return -n-1
s=1
m=0
index=None
out=[]
for i in range(len(x)):
	if x[i]==-1 or x[i]==0:
		l=-1
	elif x[i]>0:
		l=o(x[i])
	else:
		l=x[i]
	if l<=m:
		m=l
		index=i
	if l<0:
		s=s*-1
	out.append(l)

if s>0:
	print(*out)
else:
	# print(out)
	out[index]=o(out[index])
	print(*out)


