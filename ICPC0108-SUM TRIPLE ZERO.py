for t in range(int(input())):
    n=int(input())
    a =list(map(int,input().split()))
    cnt=0
    a.sort()
    for i in range(n-2):
        left=i+1
        right=n-1
        x=a[i]
        while left<right:
            if x+a[left]+a[right]==0:
                cnt+=1
                left+=1

            elif x+a[left]+a[right]<0:
                left+=1
            else: right-=1
    print(cnt)