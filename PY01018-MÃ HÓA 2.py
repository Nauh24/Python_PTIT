P='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    str=input()
    if str=='0': break
    k,s=str.split()
    k=int(k)
    res=''
    for i in s:
        res+=P[(P.find(i)+k)%28]
    print(res[::-1])
    print()
