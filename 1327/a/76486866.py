import sys
input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	# n=int(input())
	n,k=I()
	if (n-k)%2!=0:
		print("NO")
	else:
		if (n-k)//2>=k*(k-1)//2:
			print("YES")
		else:
			print("NO")
		



