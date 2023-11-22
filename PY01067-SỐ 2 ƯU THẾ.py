def check(n):
    return n.count('2') > len(n)//2
def solve(n):
    queue=['1','2']
    while n>0:
        top=queue.pop(0)
        if check(top):
            print(top,end=' ')
            n-=1
        queue.append(top+'0')
        queue.append(top+'1')
        queue.append(top+'2')
    print()
for t in range(int(input())):
    n=int(input())
    solve(n)
