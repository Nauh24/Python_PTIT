for t in range(int(input())):
    s=input()
    res=float('inf')
    number=''
    for  i in s:
        if i.isdigit():
            number+=i
        elif number!='':
            n=int(number)
            res=min(res,n)
            number=''
    if number!='':
        n=int(number)
        res=min(res,n)
    print(res)
