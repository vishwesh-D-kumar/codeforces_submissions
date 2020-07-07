def I():
	return list(map(int,input().split()))
t=int(input())
for i in range(t):
	n,k,d=I()
	shows=[0]*(k+1)
	# print(n,k,d)
	# curr_shows=[0]*(n+1)
	subs=0
	sch=I()
	for i in range(d):
		if shows[sch[i]]==0:
			subs+=1
		shows[sch[i]]+=1
	l=0
	r=d-1
	minsubs=subs
	while(r<n-1):
		shows[sch[l]]-=1
		if shows[sch[l]]==0:subs-=1
		r+=1
		l+=1

		if shows[sch[r]]==0:
			subs+=1
		shows[sch[r]]+=1
		minsubs=min(subs,minsubs)
	print(minsubs)



