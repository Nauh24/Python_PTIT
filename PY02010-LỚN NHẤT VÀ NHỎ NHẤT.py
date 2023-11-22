while True:
    n=int(input())
    if n==0: break
    a=[]
    for i in range(n):
        a.append(int(input()))
    if min(a)==max(a):
        print('BANG NHAU')
    else:
        print(min(a),max(a),end=' ')
        print()

'''
5
1
2
3
4
5
3
001
22
33333333333333333333333333333333333
3
1
1
1
0
'''