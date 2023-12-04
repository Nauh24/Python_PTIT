for t in range(int(input())):
    s=input()
    stack=[]
    cnt=0
    for i in s:
        if i=='(':
            cnt+=1
            stack.append(cnt)
            print(cnt,end=' ')
        elif i==')':
            print(stack[-1],end=' ')
            stack.pop()
    print()
'''
2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )
'''