a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())
da=abs(a1-b1)
db=abs(a2-b2)
if da!=0 and db!=0:
    if da==db or da==-db:
        print('YES')
    else:
        print('NO')
elif da!=0 or db!=0:
    print('YES')
else:
    print('NO')
