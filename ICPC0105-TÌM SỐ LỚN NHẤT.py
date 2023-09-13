for t in range(int(input())):
    s=input()
    ans=0
    number =''
    for i in s:
        if i.isdigit():
            number+=i
        elif number!='':
            n=int(number)
            ans=max(ans,n)
            number=''
    if number!='':
        n=int(number)
        ans=max(ans,n)
    print(ans)