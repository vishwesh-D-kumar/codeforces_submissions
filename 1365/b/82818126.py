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
	a=I()
	b=I()
	if a==sorted(a):
		print("Yes")
		continue
	else:
		if min(b.count(0),b.count(1))>=1:
			print('Yes')
		else:
			print("No")
	# arr=list(range(n))
	# arr.sort(key=lambda x:a[x])
	# f=True
	# print(arr)
	# for i in range(n):
	# 	if i!=arr[i] and b[i]==b[arr[i]]:
	# 		f=False
	# 		break
	# if f:
	# 	print("Yes")
	# else:
	# 	print("No")


	



