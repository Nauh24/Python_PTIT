for t in range(int(input())):
    s=input()
    for i in range(1,len(s),2):
        for j in range(int(s[i])):
            print(s[i-1],end='')
    print()