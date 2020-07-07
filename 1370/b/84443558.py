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
	n=2*int(input())
	arr=I()
	# print(arr)
	odds=[]
	evens=[]
	for i in range(n):
		if arr[i]%2:
			odds.append(i+1)
		else:
			evens.append(i+1)
	# print(odds)
	# print(evens)
	if len(odds)%2 and len(evens)%2:
		odds.pop()
		evens.pop()
	else:
		if len(odds)>len(evens):
			odds.pop()
			odds.pop()
		else:
			evens.pop()
			evens.pop()

	for i in range(len(evens)//2):
		print(evens[i],evens[len(evens)-1-i])
	for i in range(len(odds)//2):
		print(odds[i],odds[len(odds)-1-i])

	



