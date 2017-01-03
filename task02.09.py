a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())
if (abs(a1-b1)>=1) and (abs(a2-b2)>=1) and abs(a1-b1)==abs(a2-b2): #and a1>1 and a2>1 and b1>1 and b2>1 and a1<8 and a2<8 and b1<8 and b2<8:
    print('YES')
else:
    print('NO')