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
	odd=0
	even=0
	os=[]
	oidx1,oidx2,eidx=-1,-1,1
	for i in range(n):
		if arr[i]%2:
			odd+=1
			os.append(i+1)

		else:
			even+=1
			eidx=i
			break
	if even>0:
		print(1)
		print(eidx+1)
	elif odd>=2:
		print(2)
		print(os[0],os[1])
	else:
		print(-1)
	
