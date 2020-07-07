def I():return list(map(int,input().split()))

n,k=I()
p=I()

s=0
num=1
for i in range(k):
	s+=n-i

markers=[]
for i in range(n):
	if p[i]>=n-k+1:markers.append(i)

nums=1
for i in range(1,k):
	nums*=(markers[i]-markers[i-1])
	nums%=998244353
print(s,nums)