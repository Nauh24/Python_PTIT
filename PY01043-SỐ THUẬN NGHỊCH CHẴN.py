def check(s):
    for i in s:
        if int(i)%2==1:
            return False
    return True
for t in range(int(input())):
    n=input()
    for i in range(22,int(n),2):
        if len(str(i)) % 2 == 0 and str(i) == str(i)[::-1] and check(str(i)):
            print(i,end=' ')
    print()

