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
n=int(input())
arr=I()
net=sum(arr)
alice=arr[0]
arr=[(arr[i],i) for i in range(n)]

arr.sort()
idx=-1
for i in range(n):
	if arr[i][0]<=alice//2:
		idx=i
# print(idx,"###")
if idx==-1:
	coal=[(alice,0)]
else:
	coal=arr[:idx+1]+[(alice,0)]
s=sum([i[0] for i in coal])
if s>net//2:
	print(len(coal))
	print(*[i[1]+1 for i in coal])
else:
	print(0)




