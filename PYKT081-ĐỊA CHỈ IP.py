for t in range(int(input())):
    s=input().split('.')
    if len(s)!=4:
        print('NO')
        continue
    ok=True
    for i in s:
        if not i.isdigit():
            ok=False
            break
        if int(i)<0 or int(i)>255:
            ok=False
            break
    if ok:
        print('YES')
    else: print('NO')

'''
2
192.168.1.1
256.255.255.255
'''