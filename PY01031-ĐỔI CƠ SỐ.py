f=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',
   'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
   'W','X','Y','Z',]
for t in range(int(input())):
    n,b=map(int,input().split())
    s=''
    while n!=0:
        s=f[n%b]+s
        #print(s)
        n=n//b
    #print(n)
    print(s)
'''
3
10 2
2021 2
31 16
'''