a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if (a==b) and (a==c) and (b==c):
    print('3')
elif (a==b) and (a!=c) and (b!=c):
    print('2')
elif (a!=b) and (a==c) and (b!=c):
    print('2')
elif (a!=b) and (a!=c) and (b==c):
    print('2')
elif (a!=b) and (a!=c) and (b!=c):
    print('0')