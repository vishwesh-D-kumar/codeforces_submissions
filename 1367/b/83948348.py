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
	n=int(input())
	arr=I()
	evenbads=0
	oddbads=0
	for i in range(n):
		if arr[i]%2!=i%2:

			if arr[i]%2:
				oddbads+=1
			else:
				evenbads+=1
	if evenbads!=oddbads:
		print(-1)
	else:
		print(evenbads)

	



