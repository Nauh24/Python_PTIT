for t in range(int(input())):
    n=int(input())
    s=0
    for i in range(2-n%2,n+1,2):
        s+=1/i
    #print('{:6f}'.format(s))
    print('%.6f' %s)