# import sys
# input = sys.stdin.buffer.readline
# def I(): return(list(map(int,input().split())))
# def sieve(n):
# 	a=[1]*n
# 	for i in range(2,n):
# 	    if a[i]:
# 	        for j in range(i*i,n,i):
# 	            a[j]=0
# 	return a

# for __ in range(int(input())):
# 	n=int(input())
# 	p=I()
# 	arr=[0]*(n+1)
# 	for i in range(n):arr[p[i]]=i
# 	last=n-1
# 	f1=0
# 	f=0
# 	# print(arr)
# 	last=n-1
# 	f=0
# 	# print(arr)
# 	# for i in range(2,n):
# 	# 	if arr[i-1]==last and not f1:
# 	# 		last-=1
# 	# 	else:
# 	# 		f1=True
# 	# 		if arr[i]-1!=arr[i-1]:
# 	# 				f=1
# 	# 				break
# 	# 		if arr[i]==last:
# 				# f1=False
# 	# print(arr)
# 	f=0
# 	last=n-1
# 	i=1
# 	while(i<n+1):
# 		if arr[i]==last:
# 			last-=1
# 			i+=1
# 		else:
# 			prev=arr[i]
# 			c=last-arr[i]
# 			for j in range(arr[i],last+1):
# 				if p[j]!=i:
# 					f=1
# 					break
# 				i+=1
# 				c-=1
# 			print(i)
# 			if f:break
# 			last=prev-1
# 			i+=1



# 	if not f:
# 		print("Yes")
# 	else:
# 		print("No")


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
	p=I()
	arr=[0]*(n+1)
	for i in range(n):arr[p[i]]=i
	last=n-1
	f1=0
	f=0
	# print(arr)
	last=n-1
	f=0
	# print(arr)
	# for i in range(2,n):
	# 	if arr[i-1]==last and not f1:
	# 		last-=1
	# 	else:
	# 		f1=True
	# 		if arr[i]-1!=arr[i-1]:
	# 				f=1
	# 				break
	# 		if arr[i]==last:
				# f1=False
	# print(arr)
	f=0
	last=n-1
	i=1
	while(i<n+1):
		if arr[i]==last:
			last-=1
			i+=1
		else:
			prev=arr[i]
			c=last-arr[i]
			i+=1
			if i>n:
				break
			while(i<n+1 and c>0):
				if arr[i]-1!=arr[i-1]:
					f=1
					break
				i+=1
				c-=1
			last=prev-1
			# print(last,i)


	if not f:
		print("Yes")
	else:
		print("No")