a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
i=b[0]-a[0]
if i<0:
    print("NO")
else:
    j=b[1]-a[1]+i
    if j<0:
        print("NO")
    else:
        k=b[2]-a[2]+j
        if k<0:
            print("NO")
        else:
            print("YES")
