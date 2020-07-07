n,k=list(map(int,input().split()))
s=0
end=4*60-k
for i in range(1,n+1):
	s+=i*5
	if s>end:
		i-=1
		break
print(i)

