
for t in range(int(input())):
    s=input()
    tich=1
    for i in s:
        if i!='0':
            tich*=int(i)
    print(tich)