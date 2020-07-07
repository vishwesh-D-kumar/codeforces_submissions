n=int(input())
prime=[1]*(n+1)
a=1
x=[0]*(n+1)
for i in range(2,n+1):
	# print(prime)
	if prime[i]:
		# print(i)
		x[i]=a
		for j in range(2*i,n+1,i):
			prime[j]=False
			# print(prime)
			x[j]=a
		a+=1

print(*x[2:])

