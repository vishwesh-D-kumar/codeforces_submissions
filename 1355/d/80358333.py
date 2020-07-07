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

# for __ in range(int(input())):
n,s=I()
arr=[1]*n
arr[-1]+=s-n
if s<=2*n-1:
	print("NO")
else:
	print("YES")
	print(*arr)
	print(s-n)
	



