#function> a few programm
#fibonacci series:
#    0 | 1 | 1 | 2 | 3 | 5 | 8  ................................
#    x | y | z |                   z=x+y=0+1=1
#        x | y | z |


n=int(input('How many number you want?\n'
            ''
            ''))

if n==0:
    print('0');

elif n==1:
    print('')

else:
    x=0
    y=1
    print(str(x) + ',' +str(y),end='')
    for i in range(0,n-2):
        z=x+y
        print(','+str(z),end='')
        x=y
        y=z


