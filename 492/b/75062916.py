def I(): return(list(map(int,input().split())))

n,l=I()
a=I()
a.sort()
d=0
for i in range(n-1):d=max(a[i+1]-a[i],d)
# d=max(l-a[-1],d)
# d=max(a[0],d)
print(max(d/2,a[0],l-a[-1]))