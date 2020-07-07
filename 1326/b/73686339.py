def I():return list(map(int,input().split()))

n=int(input())
b=I()
a=[b[0]]
m=a[0]
for i in range(1,n):
	a.append(m+b[i])
	m=max(a[i],m)
print(*a)