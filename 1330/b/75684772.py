def I():return list(map(int,input().split()))

for __ in range(int(input())):
	n=int(input())
	arr=I()
	ans=[]
	m=max(arr)
	l1=m
	l2=n-m
	done=[0]*l1


	for i in range(l1):
		if arr[i]>l1:break
		done[arr[i]-1]=1
	if not done.count(0)>0:
		ans1=l2
		done=[0]*l2
		for i in range(l2):
			if arr[i+l1]>l2:break
			done[arr[i+l1]-1]=1
		if not done.count(0)>0:	
			ans.append([l1,l2])

	done=[0]*l2

	for i in range(l2):
		if arr[i]>l2:break
		done[arr[i]-1]=1
	if not done.count(0)>0:
		done=[0]*l1
		for i in range(l1):
			if arr[i+l2]>l1:break
			done[arr[i+l2]-1]=1
		if not done.count(0)>0 and l1!=l2:
			ans.append([l2,l1])
	print(len(ans))
	for i in ans:print(*i)









