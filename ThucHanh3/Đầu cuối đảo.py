for t in range(int(input())):
    s=input()
    dau=s[:2]
    cuoi=s[-2:]
    cuoiDao=cuoi[::-1]
    if dau==cuoiDao: print('YES')
    else : print('NO')
    # print(cuoiDao)

'''
3
12321
1234512
10233211111
'''