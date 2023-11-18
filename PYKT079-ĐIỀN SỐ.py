for t in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a=set(a)
    Max=max(a)
    Min=min(a)
    '''
    cnt=0
    for i in range(Min,Max+1):
        if i not in a:
            #print(i)
            cnt+=1
    print(cnt)
    '''
    print(Max-Min-len(a)+1)

'''
2
5
4 5 3 8 6
3
2 1 3
'''