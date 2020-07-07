def I():return list(map(int,input().split()))
 
n,k=I()
p=I()
 
s=0
num=1
for i in range(k):
	s+=n-i
f=False
nums=1
i=0
first=False
while(i<n):
	if first:
		initial=i
		i+=1
		if i==n:
			first=False
			break
		while(not p[i]>=n-k+1):
			i+=1
			if i==n:
				first=False
				break
		if first:
			final=i
			# print(initial,final)
			nums*=(final-initial)
			nums%=998244353
	else:
		if p[i]>=n-k+1:
			first=True
			continue
		i+=1
print(s,nums)