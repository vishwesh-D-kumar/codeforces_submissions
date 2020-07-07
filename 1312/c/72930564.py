from math import log 
def I():return list(map(int,input().split()))
for __ in range(int(input())):
	n,k=I()
	a=I()
	if a==[0]*n:
		print('YES')
	else:
		used=[0]*(int(log(max(a),k)+2))

		f=0
		currUsed=[]
		for ai in a:
			d=0
			c=0
			while(ai>=1):
				d=ai%k
				ai=ai//k
				if d==1:
					# print(c)
					if used[c]:
						f=1
						break
					else:
						used[c]=1
						c+=1
					continue 
				elif d==0:
					c+=1
					continue
				else:

					break
			# print(used)
			if f:
				print("NO")
				break
			if not (d==1 or d==0):
				print("NO")
				f=1
				break
		if not f:
			print("YES")
