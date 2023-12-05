#c1:
# def Try(i):
#     for j in range(1,n+1):
#         if b[j]==0:
#             a[i]=j
#             b[j]=1
#             if i==n:
#                 s=''
#                 for x in a:
#                     s+=str(x)
#                 s=s[1:]
#                 ans.append(s)
                
                
#             else:
#                 Try(i+1)
#             b[j]=0
# for t in range(int(input())):
#     n=int(input())
#     a=[0]*(n+1)
#     b=[0]*(n+1)
#     ans=[]
#     Try(1)
#     print(len(ans))
#     for i in range(len(ans)-1,-1,-1):
#         print(ans[i],end=' ')
#     print()

#c2:
import itertools


for t in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(i+1)
    d=list(itertools.permutations(a))
    d.reverse()
    print(len(d))
    for i in d:
        print(*i,sep='',end=' ')
        
    print()