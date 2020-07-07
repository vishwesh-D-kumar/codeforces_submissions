def I(): return(list(map(int,input().split())))

n=int(input())
m=int(input())
a=I()
b=I()
f=0
for i in range(n):
	if a[i]==1 or b[i]==1:
		f=1
		break
if f:
	print(-1)
else:
	minfuel=m
	for i in range(1,n-1):
		minfuel/=((1-1/a[i])*(1-1/b[i]))
	minfuel/=((1-1/a[0])*(1-1/b[0])*(1-1/a[-1])*(1-1/b[-1]))
	print(minfuel-m)

