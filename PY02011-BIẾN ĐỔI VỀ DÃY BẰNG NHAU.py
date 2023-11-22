
n=int(input())
a=list(map(int,input().split()))
min_step=10**9
tmp=-1
for i in range(n):
    step=0
    for j in range(n):
        step+=abs(a[i]-a[j])
    if step<min_step:
        min_step=step
        tmp=a[i]
print(min_step,tmp)

'''
8
13 5 8 7 9 15 26 34
'''