n=int(input())
l=list(range(2**n))
a=[0]*n
for i in range(n):
	a[i]=int(input())

for x in l:
	s=0
	for i in range(n):
		
		if (x & 1<<i):
			s+=a[i]
		else:
			s-=a[i]
	s%=360
	if s==0:
		print("YES")
		break
	# print(s,x)	
if not s==0:print("NO")

