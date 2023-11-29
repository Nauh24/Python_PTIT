n=int(input())
a=[]
while len(a)<n:
    a+=list(map(int,input().split()))
ok=True
for i in range(1,a[len(a)-1]):
    if i not in a:
        ok=False
        print(i)
if ok:
    print('Excellent!')


'''
4
1 2 3 5

7
4 5 7 8 9
10 11

5
1 2 3
4
5
'''