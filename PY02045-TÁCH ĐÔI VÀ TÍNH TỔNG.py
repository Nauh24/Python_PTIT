s=input()
while (len(s)!=1):
    i=int(len(s)/2)
    x=int(s[:(i)])
    y=int(s[(i):])
    print(x+y)
    s=str(x+y)
