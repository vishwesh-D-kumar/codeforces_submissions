y=input()
a='1111111'
b='0000000'
flag=0
for i in range(100):
    if a in y or b in y:
        flag=1
    a+='1'
    b+='0'
if flag==1:
    print('YES')
else:
    print('NO')